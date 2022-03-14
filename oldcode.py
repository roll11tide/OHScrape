"""
# Property Details
        type = soup.find("td", text="Type").find_next_sibling("td").text
        win = soup.find("td", text="WIN").find_next_sibling("td").text
        year = soup.find("td", text="Year").find_next_sibling("td").text
        length = soup.find("td", text="Length").find_next_sibling("td").text
        make = soup.find("td", text="Make").find_next_sibling("td").text
        model = soup.find("td", text="Model").find_next_sibling("td").text

        # Current Title Information
        titleNumber = soup.find("td", text="Title Number").find_next_sibling("td").text
        ownerName = soup.find("td", text="Owner Name").find_next_sibling("td").text
        issueDate = soup.find("td", text="Issue Date").find_next_sibling("td").text
        titleStatus = soup.find("td", text="Title Status").find_next_sibling("td").text
        titleType = soup.find("td", text="Title Type").find_next_sibling("td").text
        controlNumber = soup.find("td", text="Control Number").find_next_sibling("td").text
        numOwners = soup.find("td", text="Number of Owners").find_next_sibling("td").text
        resideCounty = soup.find("td", text="Resides in County").find_next_sibling("td").text
        lien1 = soup.find("td", text="Lien 1").find_next_sibling("td").text
        lien1Cancel = soup.find("td", text="Lien 1 Cancel Date").find_next_sibling("td").text
        lien2 = soup.find("td", text="Lien 2").find_next_sibling("td").text
        lien2Cancel = soup.find("td", text="Lien 2 Cancel Date").find_next_sibling("td").text
        totalPurchasePrice = soup.find("td", text="Total Purchase Price").find_next_sibling("td").text

        propertyArray = [type, win, year, length, make, model, titleNumber, ownerName, issueDate,
               titleStatus, titleType, controlNumber, numOwners, resideCounty, lien1, lien1Cancel,
               lien2, lien2Cancel, totalPurchasePrice]

    #errorsFound = len(dom.xpath('//html/body/article/section/div/section/article/div/div[1]/div[@role="alert"]'))
    #soupCheck = soup.find("td", text="Type")
    #errorDialog = dom.xpath('/html/body/article/section/div/section/article/div/div[1]/div/div/text()')

    def CleanseInput(id):
    cleanArray = []
    i = 0
    while i < len(id):
        ch = id[i]
        if not ch.islower():
            cleanArray.append(ch)
        i += 1

    clean = ''.join(cleanArray)

    clean = clean.replace('\\', '')

    return clean
"""