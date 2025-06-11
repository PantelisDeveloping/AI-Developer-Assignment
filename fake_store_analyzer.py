import requests
import json
from collections import Counter
import statistics

def fetch_products():
    """Fetch products from the Fake Store API"""
    try:
        response = requests.get('https://fakestoreapi.com/products')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def analyze_products(products):
    """Analyze the products and return results in JSON format"""
    if not products:
        return {"error": "No products data available"}
    
    # Basic statistics
    total_products = len(products)
    prices = [product['price'] for product in products]
    average_price = round(statistics.mean(prices), 2)
    
    # Most expensive and cheapest products
    most_expensive = max(products, key=lambda x: x['price'])
    cheapest = min(products, key=lambda x: x['price'])
    
    # Category analysis
    categories = [product['category'] for product in products]
    category_counts = dict(Counter(categories))
    
    # Rating analysis
    low_rating_products = []
    high_rating_products = []
    
    for product in products:
        rating = product['rating']['rate']
        if rating < 3:
            low_rating_products.append({
                'id': product['id'],
                'title': product['title'],
                'price': product['price'],
                'rating': rating,
                'category': product['category']
            })
        elif rating > 4.1:
            high_rating_products.append({
                'id': product['id'],
                'title': product['title'],
                'price': product['price'],
                'rating': rating,
                'category': product['category']
            })
    
    # Compile analysis results
    analysis_results = {
        "summary": {
            "total_products": total_products,
            "average_price": average_price,
            "price_range": {
                "min": min(prices),
                "max": max(prices)
            }
        },
        "most_expensive_product": {
            "id": most_expensive['id'],
            "title": most_expensive['title'],
            "price": most_expensive['price'],
            "category": most_expensive['category']
        },
        "cheapest_product": {
            "id": cheapest['id'],
            "title": cheapest['title'],
            "price": cheapest['price'],
            "category": cheapest['category']
        },
        "products_by_category": category_counts,
        "rating_analysis": {
            "low_rating_products_count": len(low_rating_products),
            "high_rating_products_count": len(high_rating_products),
            "low_rating_products": low_rating_products,
            "high_rating_products": high_rating_products
        }
    }
    
    return analysis_results

def main_analyzer():
    """Main analyzer function that returns JSON data"""
    print("Fetching products from Fake Store API...")
    products = fetch_products()
    
    if products:
        print(f"Successfully fetched {len(products)} products")
        print("Analyzing products...")
        
        analysis = analyze_products(products)
        
        # Optionally save to file with timestamp
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'product_analysis_{timestamp}.json'
        
        with open(filename, 'w') as f:
            json.dump(analysis, f, indent=2)
        print(f"Results saved to '{filename}'")
        
        return analysis
        
    else:
        error_result = {"error": "Failed to fetch products from API"}
        print(json.dumps(error_result, indent=2))
        return error_result

def main():
    """Main function for direct execution"""
    analysis = main_analyzer()
    
    # Output results in JSON format
    json_output = json.dumps(analysis, indent=2)
    print("\n" + "="*50)
    print("ANALYSIS RESULTS (JSON FORMAT)")
    print("="*50)
    print(json_output)

if __name__ == "__main__":
    main()