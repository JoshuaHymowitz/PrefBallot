class Ballot:


    def __init__(self, candidate_list):
        self.candidate_list = candidate_list


    def getTopValidCandidate(self, valid_candidates):
        for candidate in self.candidate_list:
            if(candidate.name not in valid_candidates):
                
                continue
            else:
                return candidate.name
    



    

    