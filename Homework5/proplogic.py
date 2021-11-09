#!/usr/bin/python3

""""
Bryan Baker
bake1358@umn.edu
CSCI 5511 - Homework 5
Propositional Logic: Basic Logic
"""

import sat_interface


def example_problem():
    print("Liars and Truth-tellers Example Problem:")
    example_prob = sat_interface.KB(["~A ~B", "B A", "~B ~C", "C B", "~C ~A", "~C ~B", "A B C"])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    if example_prob.test_literal("A") and not example_prob.test_literal("~A"):
        print("Amy is a truth-teller.")
    elif example_prob.test_literal("~A") and not example_prob.test_literal("A"):
        print("Amy is a liar.")
    else:
        print("Not enough information about Amy to decide.")
    if example_prob.test_literal("B") and not example_prob.test_literal("~B"):
        print("Bob is a truth-teller.")
    elif example_prob.test_literal("~B") and not example_prob.test_literal("B"):
        print("Bob is a liar.")
    else:
        print("Not enough information about Bob to decide.")
    if example_prob.test_literal("C") and not example_prob.test_literal("~C"):
        print("Cal is a truth-teller.")
    elif example_prob.test_literal("~C") and not example_prob.test_literal("C"):
        print("Cal is a liar.")
    else:
        print("Not enough information about Cal to decide.")
    print("")


def tt2():
    print("Liars and Truth-tellers II:")
    example_prob = sat_interface.KB(["~A C", "~A A ~C", "~B ~C", "C B", "~C B ~A", "~B C", "A C"])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    if example_prob.test_literal("A") and not example_prob.test_literal("~A"):
        print("Amy is a truth-teller.")
    elif example_prob.test_literal("~A") and not example_prob.test_literal("A"):
        print("Amy is a liar.")
    else:
        print("Not enough information about Amy to decide.")
    if example_prob.test_literal("B") and not example_prob.test_literal("~B"):
        print("Bob is a truth-teller.")
    elif example_prob.test_literal("~B") and not example_prob.test_literal("B"):
        print("Bob is a liar.")
    else:
        print("Not enough information about Bob to decide.")
    if example_prob.test_literal("C") and not example_prob.test_literal("~C"):
        print("Cal is a truth-teller.")
    elif example_prob.test_literal("~C") and not example_prob.test_literal("C"):
        print("Cal is a liar.")
    else:
        print("Not enough information about Cal to decide.")
    print("")


def tt3():
    print("Liars and Truth-tellers III:")
    example_prob = sat_interface.KB(["~A ~C", "C A", "~B A", "~B C", "~A ~C B", "~C B", "~B C"])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    if example_prob.test_literal("A") and not example_prob.test_literal("~A"):
        print("Amy is a truth-teller.")
    elif example_prob.test_literal("~A") and not example_prob.test_literal("A"):
        print("Amy is a liar.")
    else:
        print("Not enough information about Amy to decide.")
    if example_prob.test_literal("B") and not example_prob.test_literal("~B"):
        print("Bob is a truth-teller.")
    elif example_prob.test_literal("~B") and not example_prob.test_literal("B"):
        print("Bob is a liar.")
    else:
        print("Not enough information about Bob to decide.")
    if example_prob.test_literal("C") and not example_prob.test_literal("~C"):
        print("Cal is a truth-teller.")
    elif example_prob.test_literal("~C") and not example_prob.test_literal("C"):
        print("Cal is a liar.")
    else:
        print("Not enough information about Cal to decide.")
    print("")


def salt():
    print("Robbery and a Salt:")
    example_prob = sat_interface.KB(["~AT B", "~B AT", "AT A C", "~A ~AT", "~C ~AT", "~BT AT", "~AT BT"
                                            , "~CT ~C", "C CT", "A B C", "AT BT CT", "~AT ~BT ~CT"])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    if example_prob.test_literal("A") and not example_prob.test_literal("~A"):
        print("Caterpillar ate the salt.")
    elif example_prob.test_literal("~A") and not example_prob.test_literal("A"):
        print("Caterpillar did not eat the salt.")
    else:
        print("Not enough information about Caterpillar to decide.")
    if example_prob.test_literal("B") and not example_prob.test_literal("~B"):
        print("Bill the Lizard ate the salt.")
    elif example_prob.test_literal("~B") and not example_prob.test_literal("B"):
        print("Bill the Lizard did not eat the salt.")
    else:
        print("Not enough information about Bill the Lizard to decide.")
    if example_prob.test_literal("C") and not example_prob.test_literal("~C"):
        print("Cheshire Cat ate the salt.")
    elif example_prob.test_literal("~C") and not example_prob.test_literal("C"):
        print("Cheshire Cat did not eat the salt.")
    else:
        print("Not enough information about Cheshire Cat to decide.")
    print("")


def golf():
    print("An honest name:")
    example_prob = sat_interface.KB(["T", "D ~D", "~H"  # Tom tells the truth; Harry lies; unknown about Dick
                                    , "F ~H ~M", "F H M", "~H M ~T", "H ~M ~T"  # T <=> ((F <=> T) and (M <=> H)
                                    , "~D F ~H ~L ~M", "~D F H ~L M", "~D L ~T", "D F ~H L ~M", "D F H L M", "D ~L ~T", "~H M ~T", "H ~M ~T"  # T <=> ((F <=> T) and (M <=> H) and (L <=> D)
                                    , "~D ~F ~M ~T", "~D F T", "~D M T", "D ~F ~H ~M", "D ~F H T", "D F H ~M", "F ~H T"  # not T <=> ((F <=> (D or H)) and (M <=> (T or D))
                                    , "~H ~M T", "~H M ~T", "L ~M ~T", "L M T"  # H <=> ((L <=> H) and (M <=> T))
                                    , "~F ~H M", "~F H ~M", "F ~H ~M", "F H M"  # F <=> (M <=> H)
                                    , "~L ~M T", "~L M ~T", "L ~M ~T", "L M T"  # L <=> (M <=> T)
                                    , "F L M"  # (T and F) or (T and M) or (T and L)
                                    , "~H ~M TF", "~H M ~TF", "H ~M ~TF", "H M TF"  # TF <=> (M <=> H)
                                    , "~D ~M ~TM", "~D M TM", "D ~M TM", "D M ~TM"  # TM <=> not (M <=> D)
                                    , "~M ~TL T", "~M TL ~T", "M ~TL ~T", "M TL T"  # TL <=> (M <=> T)
                                    , "~H ~M ~DF", "~H M DF", "H ~M DF", "H M ~DF"  # DF <=> not (M <=> H)
                                    , "~D ~M ~DM", "~D M DM", "D ~M DM", "D M ~DM"  # DM <=> not (M <=> D)
                                    , "~M ~DL ~T", "~M DL T", "M ~DL T", "M DL ~T"  # DL <=> not (M <=> T)
                                    , "~H ~M ~HF", "~H M HF", "H ~M HF", "H M ~HF"  # HF <=> not (M <=> H)
                                    , "~D ~M HM", "~D M ~HM", "D ~M ~HM", "D M HM"  # HM <=> (M <=> D)
                                    , "~M ~HL T", "~M HL ~T", "M ~HL ~T", "M HL T"  # HL <=> (M <=> T)
                                    ])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    if example_prob.test_literal("F") and not example_prob.test_literal("~F"):
        print("The first man is telling the truth.")
    elif example_prob.test_literal("~F") and not example_prob.test_literal("F"):
        print("The first man is lying.")
    else:
        print("Not enough information about the first man to decide.")
    if example_prob.test_literal("M") and not example_prob.test_literal("~M"):
        print("The middle man is telling the truth.")
    elif example_prob.test_literal("~M") and not example_prob.test_literal("M"):
        print("The middle man is lying.")
    else:
        print("Not enough information about the middle man to decide.")
    if example_prob.test_literal("L") and not example_prob.test_literal("~L"):
        print("The last man is telling the truth.")
    elif example_prob.test_literal("~L") and not example_prob.test_literal("L"):
        print("The last man is lying.")
    else:
        print("Not enough information about the last man to decide.")
    if example_prob.test_literal("T") and not example_prob.test_literal("~T"):
        print("Tom tells the truth.")
    elif example_prob.test_literal("~T") and not example_prob.test_literal("T"):
        print("Tom lies.")
    else:
        print("Not enough information about Tom to decide.")
    if example_prob.test_literal("D") and not example_prob.test_literal("~D"):
        print("Dick tells the truth.")
    elif example_prob.test_literal("~D") and not example_prob.test_literal("D"):
        print("Dick lies.")
    else:
        print("Not enough information about Dick to decide.")
    if example_prob.test_literal("H") and not example_prob.test_literal("~H"):
        print("Harry tells the truth.")
    elif example_prob.test_literal("~H") and not example_prob.test_literal("H"):
        print("Harry lies.")
    else:
        print("Not enough information about Harry to decide.")
    if example_prob.test_literal("TF") and not example_prob.test_literal("~TF"):
        print("Tom is the first person.")
    elif example_prob.test_literal("~TF") and not example_prob.test_literal("TF"):
        print("Tom is not the first person.")
    else:
        print("Not enough information about Tom being the first person to decide.")
    if example_prob.test_literal("TM") and not example_prob.test_literal("~TM"):
        print("Tom is the middle person.")
    elif example_prob.test_literal("~TM") and not example_prob.test_literal("TM"):
        print("Tom is not the middle person.")
    else:
        print("Not enough information about Tom being the middle person to decide.")
    if example_prob.test_literal("TL") and not example_prob.test_literal("~TL"):
        print("Tom is the last person.")
    elif example_prob.test_literal("~TL") and not example_prob.test_literal("TL"):
        print("Tom is not the last person.")
    else:
        print("Not enough information about Tom being the last person to decide.")
    if example_prob.test_literal("DF") and not example_prob.test_literal("~DF"):
        print("Dick is the first person.")
    elif example_prob.test_literal("~DF") and not example_prob.test_literal("DF"):
        print("Dick is not the first person.")
    else:
        print("Not enough information about Dick being the first person to decide.")
    if example_prob.test_literal("DM") and not example_prob.test_literal("~DM"):
        print("Dick is the middle person.")
    elif example_prob.test_literal("~DM") and not example_prob.test_literal("DM"):
        print("Dick is not the middle person.")
    else:
        print("Not enough information about Dick being the middle person to decide.")
    if example_prob.test_literal("DL") and not example_prob.test_literal("~DL"):
        print("Dick is the last person.")
    elif example_prob.test_literal("~DL") and not example_prob.test_literal("DL"):
        print("Dick is not the last person.")
    else:
        print("Not enough information about Dick being the last person to decide.")
    if example_prob.test_literal("HF") and not example_prob.test_literal("~HF"):
        print("Harry is the first person.")
    elif example_prob.test_literal("~HF") and not example_prob.test_literal("HF"):
        print("Harry is not the first person.")
    else:
        print("Not enough information about Harry being the first person to decide.")
    if example_prob.test_literal("HM") and not example_prob.test_literal("~HM"):
        print("Harry is the middle person.")
    elif example_prob.test_literal("~HM") and not example_prob.test_literal("HM"):
        print("Harry is not the middle person.")
    else:
        print("Not enough information about Harry being the middle person to decide.")
    if example_prob.test_literal("HL") and not example_prob.test_literal("~HL"):
        print("Harry is the last person.")
    elif example_prob.test_literal("~HL") and not example_prob.test_literal("HL"):
        print("Harry is not the last person.")
    else:
        print("Not enough information about Harry being the last person to decide.")
    print("")


def main():
    example_problem()
    tt2()
    tt3()
    salt()
    golf()


if __name__ == "__main__":
    main()
