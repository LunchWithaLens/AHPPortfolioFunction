# Azure Portfolio Function

Azure python based AHP Portfolio function to get weights in Analytic Hierarchy Process
The format of the matrix being sent over will be like {"matrix":"1,A,B,c,C,C,a,1,A,c,B,C,b,a,1,c,B,C,C,C,C,1,C,C,c,b,b,c,1,A,c,c,c,c,a,1"}
The matrix represents the relationship between projects - 1 is identity or equally important, 0 is no relationship, 
then c, b, a, A, B, C represent extremely less important than up to extremely more important than.

The return value is like {"pev":  "7.3497505", "weights" : "[0.1916 0.1053 0.0718 0.5863 0.0268 0.0181]", "cr" : "0.7837"} 
where weights are the relative ranking of the projects cr is the consitency raio and pev is the principal eigen value.

Target is Python 3.9
