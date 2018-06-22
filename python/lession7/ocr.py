
import csv
import string
from PIL import Image
import pytesseract
from form import register

REGISTER_URL = 'http://example.webscraping.com/user/register'

def main():
	print register()