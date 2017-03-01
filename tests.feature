
Feature: Place speaker 102-1550-ND in shopping cart (Functional)
As a consumer
I want to be able to place speaker 102-1550-ND in my shopping cart 
So I can purchase that speaker as a part of my future order.

Normal Flow:
  Scenario: Place speaker 102-1550-ND in the shopping cart for a quantity at least 1
    Given	I am at Digi-Key Electronics product page of speaker 102-1550-ND
     When 	I input a quantity of 2  and click add to shopping cart
     Then	It will redirect to the shopping cart page where you can find the speaker with part number of 102-1550-ND in the shopping cart.
  
  Alternative Flow:
  Scenario: Place speaker 102-1550-ND in the shopping cart for a quantity at least 1 from the shopping cart page
    Given	I am at Digi-Key Electronics page showing my shopping cart
     When 	I input a quantity of 2 and part number 102-1550-ND click add to cart 
     Then	The shopping cart page will update with speaker 102-1550-ND with quantity 2
  
  Error Flow:
  Scenario: Place speaker 102-1550-ND in the shopping cart for a negative quantity
    Given	I am at Digi-Key Electronics product page of speaker 102-1550-ND
     When 	I input a quantity of -2  and click add to shopping cart
     Then	It will reload the page and should indicate invalid value