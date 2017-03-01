Feature: Place Oster blender in shopping cart (Functional)

As a consumer I want to be able to place the Oster blender in my shopping cart so I can purchase that blender as a part of my future order.

  Scenario: Place 2 Oster Blenders in the shopping cart
  
    Given I am at ebay product page for the Oster blender "http://www.ebay.ca/itm/161728962861"
     When   I input a quantity of "2" into textbox "qtyTextBox" and click the "isCartBtn_btn"
     Then It will redirect to the shopping cart page where you can find the product from the product page "http://www.ebay.ca/itm/161728962861" with quantity "2"
  
  Scenario: Place speaker 102-1550-ND in the shopping cart for a quantity at least 1 from the shopping cart page
    Given I am at Digi-Key Electronics page showing my shopping cart
     When   I input a quantity of 2 and part number 102-1550-ND click add to cart 
     Then The shopping cart page will update with speaker 102-1550-ND with quantity 2
  
  Scenario: Place speaker 102-1550-ND in the shopping cart for a negative quantity
    Given I am at Digi-Key Electronics product page of speaker 102-1550-ND
     When   I input a quantity of -2  and click add to shopping cart
     Then It will reload the page and should indicate invalid value