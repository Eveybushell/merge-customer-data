# merge-customer-data

## Clarifying Questions
Is each customer ID unique?<br>
Can the same customer ID be in both integer arrays and if so, how should I handle them?<br>
How do we want to handle a type mismatch on the input?<br>

## Time and Space Complexity
The time complexity should be O(n). I am looping through both arrays a single time so the run time is O(m+n)<br>
The space complexity should be O(1). I am only creating 3 integer variables and updating them.