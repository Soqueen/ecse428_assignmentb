Feature: Place Oster blender in shopping cart (Functional)

  As a consumer I want to be able to place the Oster blender in my shopping cart so I can purchase that blender as a part of my future order.

  Scenario: Place 'Oster White 8 Speed Blender - BLSTMG-W00-033' in the shopping cart with quantity of 1 or more
    Given   I am at the ebay product page for the Oster blender "http://www.ebay.ca/itm/161728962861"
    When   I input a quantity of "2" and add to shopping cart
    Then   It will redirect to "Your eBay Shopping Cart" page
    And    The "Oster White 8 Speed Blender - BLSTMG-W00-033" is in the cart
    And    Its quantity is equal to "2"

  Scenario: Update 'Oster White 8 Speed Blender - BLSTMG-W00-033' in the shopping cart for another quantity
    Given   I am at the shopping cart page "http://cart.payments.ebay.ca/sc/view"
    When   I edit the quantity to "5" and click update
    Then   It will reload the page and show the new quantity "5"

  Scenario: Place 'Oster White 8 Speed Blender - BLSTMG-W00-033' in the shopping cart with less than 1
    Given   I am on the ebay product page for the Oster blender "http://www.ebay.ca/itm/161728962861"
    When   I input an invalid quantity of "-2"
    Then   It should indicate error "Please enter quantity of 1 or more"