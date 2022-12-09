from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from dotenv import load_dotenv

load_dotenv()


service = Service(executable_path=ChromeDriverManager().install())
