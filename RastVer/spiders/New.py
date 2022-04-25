
class New:
    def __init__(self, rate='None', claim='None'):
        self.rate = rate
        self.claim = claim

    def validation(self, hard=False):
        if self.rate == None:
            return False
        elif self.claim == None:
            return False

        #Validation that checks the content of the fields to avoid deteccion error
        if hard == False:
            return True
        else:
            #Somtiemes it has detected the element before the claim and usually this ends in ":
            if list(self.claim).pop == ':':
                return False


    def print(self):
        return str(self.rate) + "," + str(self.claim) + ",\n"