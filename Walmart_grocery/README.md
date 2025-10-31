## Problem Statement

**Develop a Python-based Walmart Grocery Management System** that simulates an online grocery shopping experience, allowing users to:

1. **Browse and search** for grocery products across categories
2. **Add/remove items** to/from a shopping cart
3. **Manage user accounts** with registration and login functionality
4. **Process orders** with inventory management
5. **Generate receipts** and order summaries
6. **Maintain persistent data storage** for products, users, and orders

## Key Features Implemented

### 1. **Product Management**
- Categorized products (Fruits, Vegetables, Dairy, etc.)
- Product details (name, price, quantity, category)
- Inventory tracking and stock updates

### 2. **User Management**
- User registration and authentication
- Profile management
- Order history tracking

### 3. **Shopping Cart System**
- Add/remove items from cart
- Quantity management
- Price calculation
- Cart persistence

### 4. **Order Processing**
- Checkout functionality
- Inventory validation
- Receipt generation
- Order confirmation

### 5. **Data Persistence**
- JSON-based data storage
- File handling for users, products, and orders
- Data consistency maintenance

## Technical Architecture

### Core Modules:
- **`main.py`** - Application entry point and menu system
- **`user.py`** - User management and authentication
- **`product.py`** - Product catalog and inventory management
- **`cart.py`** - Shopping cart operations
- **`order.py`** - Order processing and receipt generation

### Data Storage:
- `users.json` - User accounts and profiles
- `products.json` - Product catalog and inventory
- `orders.json` - Order history and tracking

## Key Challenges Solved

1. **Data Integrity** - Ensuring consistent state across multiple JSON files
2. **Inventory Management** - Real-time stock updates during purchases
3. **User Session Management** - Maintaining cart state across user sessions
4. **Input Validation** - Handling various user input scenarios
5. **Error Handling** - Graceful management of file operations and data corruption

## Business Logic Flow

```
User Registration/Login → Browse Products → Add to Cart → 
Checkout → Inventory Check → Order Confirmation → Receipt Generation
```

## Technical Strengths

- **Modular Design** - Separated concerns across different classes
- **Data Persistence** - JSON-based storage for simplicity
- **Input Validation** - Comprehensive error checking
- **Inventory Control** - Real-time stock management
- **Receipt System** - Detailed order summaries

This project effectively simulates a real-world e-commerce grocery system with proper inventory management, user authentication, and order processing capabilities.
