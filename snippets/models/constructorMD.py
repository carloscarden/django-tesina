

from snippets.models.mockLel import MockLel


class ConstructorMD:
    """A simple example class"""
    i = 12345

    def construirMD(self):
        mock = MockLel()
        lels = mock.lelMockeado()

        print("aplico la regla 1 y me quedo con el conjunto de facts")
        facts = self.regla1(lels)


        niveles = []
        medidas = []
        dimensiones = []
        for f in facts :
            print("aplico regla2 y me quedo con el conjunto de medidas")
            medidas = self.regla2()
            print("aplico regla 3 y me quedo con el conjunto de dimensiones")
            niveles = self.regla3()

    """

        Require: a LEL  
        Ensure: 
         set of facts F, 
         sets of measures/dimensions Mf , 
         Df ∀f ∈ F, 
         set of levels L
        
        1: apply Rule 1 to the LEL, get set F of facts
        2: L ← ∅
        3: for each f ∈ F, corresponding to verb v: do
        4:       apply Rule 2 to v, get set Mf of measures, add them to f
        5:       apply Rule 3 to v, get set Df of dimensions, add them to f
        6:       L ← L U Df
        7: end for

        8: repeat
        9:   for each l ∈ L, corresponding to object/subject o: do
        10:       apply Rule 4 to o, get set Cl of levels, add them to l as children levels
        11:       apply Rule 5 to o, get set Pl of properties, add them to l as children levels
        12:       for each l' ∈ Cl, corresponding to object/subject o': do
        13:           apply Rule 6 to o and o', possibly change the arc from l to l' to multiple
        14:           apply Rule 7 to o and o', possibly change the arc from l to l' to optional
        15:       end for
        16:       L :← L \ {l} U Cl
        17:  end for
        18: until no new levels are added to L
        19: return F, L, {Mf , f ∈ F}, {Df , f ∈ F}
      """

    def regla1(self, lels):
        # Rule1:  Verbs give origin to facts:
        ". Let v be a verb of the LEL, then v should be defined as a fact"

        # Justification:
        """ The verbs of the glossary describe the activities of the organization. 
        A fact corresponds to an activity that occurs in the organization,and end-users are 
        interested in monitoring and analyzing
        """
        return 'hello world'

    def regla2(self):
        # Rule2: Numerical objects and subjects of verbs give origin to measures
        """
        .. Let v be a verb defined as a fact according to Rule 1 
        .. and n be its notion. 
        .. Let M be the set of objects and subjects in n that denote numerical attributes, 
        -------> 
           then all the elements in M should be defined as measures of the fact corresponding to v.
        """

        # Justification
        """ 
        Measures quantify occurrences of facts. 
        Objects and subjects describe attributes or characteristics of activities. 
        Numerical objects andsubjects are candidates to be measures"""

        return 'regla2'

    def regla3(self):
        # Rule 3. Categorical objects and subjects of verbs give origin to dimensions.
        """
        Let v be a verb defined as a fact according to Rule 1 and n be its notion. 
        Let D be the set of objects and subjects in n that denote categorical attributes, 
        -----> then the elements on D should be defined as dimensions of the fact corresponding
        to b 
        """

        # Justification:
        """
        Dimensions are categorical attributes that act as coordinates for facts. 
        Objects and subjects describe attributes or characteristics of activities. 
        Non-numerical objects and subjects are candidates to be dimensions"""
        return 'regla3'

    def regla4(self):

        # Rule 4. Categorical objects and subjects of objects or subjects give origin to levels.

        """
        Let o be an object or subject defined 
                 as a dimension (according toRule 3) 
                 or level (according to Rule 4) 
        and n be its notion. 
        
        Let L be the set of objects and subjects in n that 
           (i) have not been defined as dimensions,  
           (ii) denote categorical attributes, and 
           (iii) are related to o by aggregation semantics; 
        
        ---> then the elements in L should be defined as children levels of o"""

        # Justification
        """
        The different levels within a hierarchy are related by associations expressing aggregation. 
        Objects and subjects in the notion of an object or subject may describe aggregation 
        relationships using synonyms such as belongs to, is comprised by, and has a. 
        Other relation semantics such as constitutes, is covered by, is incorporated in, involves,
         etc. can also give origin to aggregations"""
        return 'regla4'

    def regla5(self):

        # Rule 5. Numerical objects and subjects of objects or subjects give origin to properties.
        """ 
        Let o be an object or subject defined as a dimension or level according to Rules 3 or 4 
        and n be its notion. 
        Let L be the set of objects and subjects in n that denote numerical attributes, 
        ---> then the elements in L should be defined as properties of o"""

        # Justification

        """
        Properties give further descriptions of a level. 
        Notions state descriptions of the symbol, typically characteristics of a subject or object.
        It is common to use the verb “has”, “possess”, “owns” or a synonym
        """
        return 'regla5'

    def regla6(self):
        # Rule 6. Plural objects and subjects give origin to multiple arcs.
        """
        Let o be an object or subject defined as a dimension or level, 
        n be its notion, and o' an object or subject in n defined as a child level of o. 
        If o' is plural, then the arc from o to o' is a multiple one."""

        # Justification
        """
        Natural language expresses relationship cardinalities in an accurate way. 
        For example, in the expression “entity-1 belongs to one or more entity-2”, 
        entity-2 should be plural, thus it clearly defines the cardinality towards entity-2. 
        Nevertheless, the reciprocal cardinality cannot be inferred, unless it is explicitly stated."""
        return 'regla6'

    def regla7(self):
        # Rule 7. Expressions of possibility in objects and subjects determine optional arcs.
        """ 
        .. Let o be an object or subject defined as a dimension or level, 
        .. n be its notion, 
        .. and o' an object or subject in n defined as a child level of o.

        If the verb used in n to relate o with o' suggests that some instances of o 
        may not be associated to every instance of o', then the arc from o to o' is an optional one
        """

        return 'regla7'
