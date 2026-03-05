# BoyGirlParadox
The code is designed to make a pool of "families", all with two children. From that pool, we randomly select a family.  Within that family, we will be randomly told about one of the children.  We will then look at what the other child is.  A counter is maintained that records the total of all outcomes.  We track how many first told us about a girl, and the other child is a boy.  We then track how many first told us about a girl and the other child is a girl.  The results of being told about a boy first are also tracked.

The result is a proof that the Boy Girl Paradox predicted rates of 66% is wrong, and that the results are actually 50/50. 


# Test Results:
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


If you group the possibilities into BB, BG, GB, and GG then run the probabilities, then out of the three groups with at least one boy 2/3 of them will have a girl for the second child. 66% does seem like the right answer based on some very simple probability calculations.

The issue is that these selections actually don't reflect the real world incidences.  In the previous calculations, we have assigned equal probability to the scenarios of BB, BG and GB pairs.  This is not actually the case. For example, we have to consider how much more likely a mom with two boys is likely to tell you about one of her boys, as compared to someone with a boy and a girl. The mother with two boys will always tell you about one of her boys, while the mothers in the boy/girl pairs are only 50% likely to mention they have a boy.  The other half of the time, they will mention their girl.  If we use expected value calculations, we actually get correct answers. Here is the proof.


Let's say we have 200 children in two child households


50 GG

50 BG

50 GB

50 BB


0% of GG households will (randomly) first tell you about one child who is a boy.

50% of BG households will (randomly) first tell you about a child who is a boy (the other 50% of the time, they mention the girl)

50% of GB households will (randomly) first tell you about a child who is a boy (the other 50% of the time, they mention the girl)

100% of BB households will (randomly) first tell you about a child who is a boy



So when this scenario starts, we have:


25 BG households

25 GB households

50 BB households

*note the unequal distribution of each group.


Only the BB group will tell you they have a second boy, which is 50/100. The odds are 50%, which oddly enough is the intuitive answer.

It really is sort of crazy, that because of a simple misuse of statistics people will believe that the words used (whether they say one of their children is a boy vs saying their first child is a boy) will actually effect the odds of what the second child are. That is such an obviously wrong assertion... literally everyone knows thay is wrong (at first) but all it takes is a little bit of misapplied math and everyone believes it. 


# When are the 2/3 and 1/3 probabilities applicable?

  So when would the odds of the second boy be 1/3? Well, they would certainly be true when there is a survey. If you were to make a survey and send it to 10,000 parents with at least one boy, then you would get the classical results.  In fact, this survey is a common proof of the classical answer.  It's important to note though, that by asking the question yourself, you are making a selection.  You are grouping and dividing up the  set of families based on your own criteria.  That is perfectly fine, as long as we realize that this doesn't model a real life scenario where information is randomly presented to us.  

  Could the 1/3 and 2/3 odds appear in real life scenarios? Yes, this *can* happen. It requires someone to *ask* the question "do you have at least one boy" (as opposed to the information being given to you). This is the same scenario as above where you are polling or surveying people to get their answer.  This is probably the most non-intuivie fact in statistics - whether you ask the question, or are randomly presented with the information, may actually alter the probabilities.

  The only way you can be organically presented with the information and get the 1/3 and 2/3 probabilities is if there is selection bias from the source.  For instance, if there was a patriarchal society where every parent always spoke of their boy first (if they had one), then you'd get the probability of the other child being a boy as 1/3 . Of course, the consequence of this patriarchal preference is that every time you hear about a girl first, the odds that the other child is also a girl is 100%.  You would only hear a parent mention a girl if they did not have a boy, so the other child would have to be a girl as well.

  Another interesting fact is that, in the scenarios where you are randomly given the information, the words used to present the information do not actually matter.  The parents could say they have "at least one boy" or "my oldest is a boy", and it actually doesn't change the probability calculation.  What actually matters is the process by which the selection occurs.  When a parent selects a random child and tells you about them, they can be as specific or vague as they want.  It doesn't matter if they say "I have at least one boy", "I have at least one boy, born on a Tuesday", or "my youngest is a boy".  The selection of the boy wasn't based on any of that... so it doesn't effect the probabilities. Likewise, in the scenario with a patriarchal preference, the selection also isn't based on any of that information.  The parent is simply selecting a boy to inform you about first, provided they have a boy to mention. 

  In the scenarios where you ask or poll for the information, all the criteria you use to make a selection will influence the probability.  This is why you get a different answer when you select familieis with "at least one boy, born on a Tuesday" (51.7%).  The reason for this is that *you* are are defining the selection. This means *you* are determining what families are selected, whether the criteria is relevant or not to a real world situation. It's worth noting that the 51.7% can't actually occur in the real world, when we allow the information to emerge naturaly, without any interaction from us. 
