class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if not senate:
            return ""
        d_votes = 0
        r_votes = 0
        current_senate = senate
        while ("R" in current_senate and "D" in current_senate):
            next_senate = ""
            for person in current_senate:
                if person == "D":
                    if r_votes >0:
                        r_votes -= 1
                    else:
                        d_votes += 1
                        next_senate += "D"
                if person == "R":
                    if d_votes > 0:
                        d_votes -= 1
                    else:
                        r_votes += 1
                        next_senate += "R"
            current_senate = str(next_senate)

        if current_senate[0] == "D":
            return "Dire"
        else:
            return "Radiant"