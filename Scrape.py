from bs4 import BeautifulSoup
import requests
from lxml import etree

def PullCSV(id):
    # Make request
    apiKey = {'WaterCraftIDSearchTerm': id}
    x = requests.post('https://bmvonline.dps.ohio.gov/Search/WatercraftIDSearch', apiKey)

    # Format HTML
    soup = BeautifulSoup(x.text, 'html.parser')
    dom = etree.HTML(str(soup))

    # Get properties
    properties = GetProperties(dom)

    # Validity check
    # If a single property actually has a value, a record was ALMOST CERTAINLY found
    empty = True
    for p in properties:
        if p != '':
            empty = False

    if empty:
        # Bad record
        print("[PULL] Fail: " + str(id))

        return 'BAD RECORD'
    else:
        csv = GenerateCSV(properties)
        print("[PULL] Success: " + str(id))
        return csv

def GenerateCSV(properties):
    # Cobble line together one property at a time
    csvString = ''
    for x in properties:
        # x.replace("\"", "\\\"")
        csvString += '\"' + x + '\"' + ','

    # Remove last character
    csvString = csvString[:len(csvString) - 1]

    return csvString

def GetProperties(dom):
    # Property Details
    vesselType = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[1]/table/tbody/tr[1]/td[2]//text()'))
    win = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[1]/table/tbody/tr[1]/td[4]//text()'))
    year = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[1]/table/tbody/tr[2]/td[2]//text()'))
    length = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[1]/table/tbody/tr[2]/td[4]//text()'))
    make = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[1]/table/tbody/tr[3]/td[2]//text()'))
    model = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[1]/table/tbody/tr[3]/td[4]//text()'))

    # Current Title Information
    titleNumber = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[1]/td[2]//text()'))
    ownerName = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[1]/td[4]//text()'))
    issueDate = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[2]/td[2]//text()'))
    titleStatus = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[2]/td[4]//text()'))
    titleType = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[3]/td[2]//text()'))
    controlNumber = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[3]/td[4]//text()'))
    numOwners = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[4]/td[2]//text()'))
    resideCounty = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[4]/td[4]//text()'))
    lien1 = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[5]/td[2]//text()'))
    lien1Cancel = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[5]/td[4]//text()'))
    lien2 = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[6]/td[2]//text()'))
    lien2Cancel = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[6]/td[4]//text()'))
    totalPurchasePrice = SafeAssign(dom.xpath('/html/body/article/section/div/div/section/article/div/div[2]/table/tbody/tr[7]/td[2]//text()'))

    propertyArray = [vesselType, win, year, length, make, model, titleNumber, ownerName, issueDate,
                     titleStatus, titleType, controlNumber, numOwners, resideCounty, lien1, lien1Cancel,
                     lien2, lien2Cancel, totalPurchasePrice]

    return propertyArray

def SafeAssign(xpathObj):
    if (len(xpathObj) == 0):
        return ''
    else:
        return xpathObj[0]