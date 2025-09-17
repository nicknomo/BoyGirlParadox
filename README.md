# BoyGirlParadox
Proof code that the Boy Girl Paradox predicted rates of 66% are wrong, and that the results are actually 50/50.

Results of a random run:


Sample Size: 100000


When first child mentioned is a GIRL:

  Total cases: 49992
  
  Girl then Girl: 24794 (0.496)
  
  Girl then Boy: 25198 (0.504)
  

When first child mentioned is a BOY:

  Total cases: 50008
  
  Boy then Boy: 25045 (0.501)
  
  Boy then Girl: 24963 (0.499)
  



# Reasoning For The Difference Between The Proclaimed 66% Answer

The Boy/Girl Paradox scenario initially states how a mother tells you about one of her children that is a boy.  It then asks what are the odds the second child is a girl? The statistical answer commonly supported is 66%.  This common answer and explanation to the boy girl paradox is actually built upon an error, and is a good illustration of how selection bias creeps into statistics in seemingly benign situations. 


If you group the possibilities into BB, BG, GB, and GG then run the probabilities, then out of the three groups with at least one boy 2/3 of them will have a girl for the second child. 66% does seem like the right answer based on some very probability calculations.


The issue is that these selections actually don't reflect the real world incidences.  In the previous calculations, we have assigned equal probability to the scenarios of BB, BG and GB pairs.  This is not actually the case. For example, we have to consider how much more likely a mom with two boys is likely to tell you about one of her boys, as compared to someone with a boy and a girl. The mother with two boys will always tell you about one of her boys, while the mothers in the boy/girl pairs are only 50% likely to mention they have a boy.  The other half of the time, they will mention their girl.  If we use expected value calculations, we actually get correct answers. Here is the proof.


Let's say we have 200 children in two child households


50 GG

50 BG

50 GB

50 BB


0% of GG households will (randomly) first tell you about one child who is a boy.

50% of BG households will (randomly) first tell you about a child who is a boy (the other 50% of the time, they mention the girl)

50% of GB households will (randomly) first tell you about a child who is a boy

100% of BB households will (randomly) first tell you about a child who is a boy



So when this scenario starts, we have:


25 BG households

25 GB households

50 BB households

*note the unequal distribution of each group.


Only the BB group will tell you they have a second boy, which is 50/100. The odds are 50%, which oddly enough is the intuitive answer.

So, let it be known that humans have trouble with statistics. All the people who tell you its 66% know just enough statistics to be dangerous.

It really is sort of crazy, that because of a simple misuse of statistics people will believe that the words used (whether they say one of their children is a boy vs saying their first child is a boy) will actually effect the odds of what the second child are. That is such an obviously wrong assertion... literally everyone knows thay is wrong (at first) but all it takes is a little bit of bad math and everyone believes it. 
