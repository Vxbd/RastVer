
class New:
    clases = ["TRUE", "MOSTLY-TRUE", "MOSTLY-FALSE", "FALSE", "BLATANT-LIE", "NO-EVIDENCE"]

    def __init__(self, rate='None', claim='None'):
        self.rate = rate.upper().replace(" ", "-")
        self.claim = claim

    def validation(self, hard=False):
        if not self.rate in New.clases:
            return False
        elif self.claim == None:
            return False
        elif self.claim == 'None':
            return False
        elif self.claim == '\n':
            return False

        s = self.claim.split(" ")
        if len(s) < 3:
            return False


        #Validation that checks the content of the fields to avoid deteccion error
        if hard == False:
            return True
        else:
            #Somtiemes it has detected the element before the claim and usually this ends in ":
            if list(self.claim).pop == ':':
                return False


    def print(self):
        return "\"" + str(self.rate).replace('\n', ' ') + "\" " + "\"" + str(self.claim).replace('\n', ' ').replace('\"', '') + "\"\n"