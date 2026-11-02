Problem Statement:
52. Hackathon Team Formation and Ranking: Analyse student scores and team compositions, validate team sizes, aggregate round-wise scores, and resolve tied rankings using predefined rules.

Algorithm:
Step 1: Start
Step 2: Read number of teams
Step 3: For each team, read Team Name, Members, Individual Scores, Round1, Round2, Round3
Step 4: Validate Team Size
       If Size < 2 or Size > 4 Then Invalid Team, go to next team
Step 5: Calculate Total Score = Round1 + Round2 + Round3
Step 6: Calculate Average Score = Sum of Individual Scores / Team Size
Step 7: Store valid teams in list
Step 8: Sort list by Total Score Descending
Step 9: If Tie, apply rules:
       Rule 1: Higher Round 3 Score gets higher rank
       Rule 2: If still tie, Higher Average Score gets higher rank
       Rule 3: If still tie, Alphabetical order of Team Name
Step 10: Assign ranks and display result
Step 11: Stop

Flowchart:
Start
  |
  v
Input Team Details
  |
  v
Is Team Size >=2 and <=4 ?
  | No -> Print Invalid Team -> Next Team
  | Yes
  v
Total = R1 + R2 + R3
  |
  v
Average = Sum / Size
  |
  v
Store Team Data
  |
  v
More Teams?
  | Yes -> Input Next Team
  | No
  v
Sort by Total Score
  |
  v
Check Tie?
  | Yes -> Apply Tie Breaker R3 > Average > Name
  | No
  v
Assign Rank
  |
  v
Display Final Ranking
  |
  v
Stop
