package ShopCart;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;

public class FitnessTestShopCart {
	WebDriver driver;

	// Constructor method
	public FitnessTestShopCart(String browser) {
		if (browser.equalsIgnoreCase("*iexplore")) {
			driver = new InternetExplorerDriver();
			driver.manage().timeouts().implicitlyWait(3, TimeUnit.SECONDS);
		} else if (browser.equalsIgnoreCase("*firefox")) {
			driver = new FirefoxDriver();
		} else if (browser.equalsIgnoreCase("*chrome")) {

			System.setProperty(
					"webdriver.chrome.driver",
					"/Users/sokhenglim/Desktop/ecse428_assignmentb/cucumber/tests/features/chrome_driver/chromedriver_mac");
			driver = new ChromeDriver();
		}
	}

	public boolean open(String URL) {
		driver.get("http://" + URL);
		return true;
	}

	public boolean type(String id, String value) {
		try {
			WebElement searchBox = driver.findElement(By.id(id));
			searchBox.clear();
			searchBox.sendKeys(value);
			return true;
		} catch (NoSuchElementException e) {
			return false;
		}
	}

	public boolean click(String id) {
		try {
			driver.findElement(By.id(id)).click();
			return true;
		} catch (NoSuchElementException e) {
			return false;
		}
	}

	public boolean verifyShopCartPage(String name) {
		return (name.equals(driver.findElement(By.id("PageTitle"))
				.findElement(By.tagName("h1")).getText().toString()));
	}

	public boolean verifyCartProductName(String name, String id) {
		return (name.equals(driver.findElement(By.id(id)).getText().toString()
				.trim()));
	}

	public boolean verifyCartProductQuantity(String quantity) {
		return (quantity.equals(driver
				.findElement(By.xpath("//input[contains(@id,'qty')]"))
				.getAttribute("value").toString().trim()));
	}

	public boolean verifyErrorMessage(String msg, String id) {
		return (msg.equals(driver.findElement(By.id(id)).getText().toString()
				.trim()));
	}

	public boolean close() {
		driver.quit();
		return true;
	}

}
