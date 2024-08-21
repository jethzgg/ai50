def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    prob = 1.0
    probs = {person:1 for person in people}
    for person in people:
        mother = people[person]["mother"]
        father = people[person]["father"]
        if not people[person]["father"] and not people[person]["mother"]:
            if person in one_gene:
                probs[person] *= PROBS["gene"][1]
                if person in have_trait:
                    probs[person] *= PROBS["trait"][1][True]
                else:
                    probs[person] *= PROBS["trait"][1][False]
            elif person in two_genes:
                probs[person] *= PROBS["gene"][2]
                if person in have_trait:
                    probs[person] *= PROBS["trait"][2][True]
                else:
                    probs[person] *= PROBS["trait"][2][False]
            else:
                probs[person] *= PROBS["gene"][0]
                if person in have_trait:
                    probs[person] *= PROBS["trait"][0][True]
                else:
                    probs[person] *= PROBS["trait"][0][False]
        else:
            mother_genes = (mother in one_gene) + 2 * (mother in two_genes)
            father_genes = (father in one_gene) + 2 * (father in two_genes)
            if person in one_gene:
                if mother_genes == 0 and father_genes != 0:
                    p = PROBS["mutation"] * PROBS["mutation"] + (1-PROBS["mutation"]) * (1-PROBS["mutation"])
                elif mother_genes != 0 and father_genes == 0:
                    p = PROBS["mutation"] * PROBS["mutation"] + (1-PROBS["mutation"]) * (1-PROBS["mutation"])
                elif mother_genes != 0 and father_genes != 0:
                    p = PROBS["mutation"] * (1-PROBS["mutation"]) * 2
                else:
                    p = PROBS["mutation"] * (1-PROBS["mutation"]) * 2
                if person in have_trait:
                    probs[person] *= PROBS["trait"][1][True] * p
                else:
                    probs[person] *= PROBS["trait"][1][False] * p
            elif person in two_genes:
                if mother_genes == 0 and father_genes != 0:
                    p = PROBS["mutation"] * (1-PROBS["mutation"])
                elif mother_genes != 0 and father_genes == 0:
                    p = PROBS["mutation"] * (1-PROBS["mutation"])
                elif mother_genes != 0 and father_genes != 0:
                    p = (1 - PROBS["mutation"]) * (1 - PROBS["mutation"])
                else:
                    p = PROBS["mutation"] * PROBS["mutation"]
                if person in have_trait:
                    probs[person] *= PROBS["trait"][2][True] * p
                else:
                    probs[person] *= PROBS["trait"][2][False] * p
            else:
                if mother_genes == 0 and father_genes != 0:
                    p = (1-PROBS["mutation"]) * PROBS["mutation"]
                elif mother_genes != 0 and father_genes == 0:
                    p = (1-PROBS["mutation"]) * PROBS["mutation"]
                elif mother_genes != 0 and father_genes != 0:
                    p = PROBS["mutation"] * PROBS["mutation"]
                else:
                    p = (1 - PROBS["mutation"]) * (1 - PROBS["mutation"])
                if person in have_trait:
                    probs[person] *= PROBS["trait"][0][True] * p
                else:
                    probs[person] *= PROBS["trait"][0][False] * p
    for key in probs:
        prob *= probs[key]            
    return prob


    