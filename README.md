A number library written in Python
===

###To use the library, open a Python shell and import the library usting its filename without the '.py' extension
```
import numLib
```

###It has the following functions: 

1. **numToWords**
  * <p>Accepts  a  whole  number from zero (0) to 1 million (1000000; without commas for example: 1,000,000) <br/>and prints on screen number in  word form</p>

  ######To call the function:
  ```
  numLib.numToWords(number)
  ```

2. **numberDelimited**
  * <p>Accepts three arguments: 
  <ul>
    <li>a  whole  number from zero (0) to 1 million (1000000; without commas for example: 1,000,000)
    <li>single character delimiter to be used
    <li>number of jumps when the delimiter will appear (from rightmost digit)
  </ul>
</p>
  * <p>Returns number delimited from from the rightmost digit</p>

  ######To call the function:
  ```
  numLib.numberDelimited(number,delimiter,jump)
  ```

3. **wordsToNum**
  * <p>Accepts a number in word form (lowercase) and returns it in numerical form</p>

  ######To call the function:
  ```
  numLib.wordsToNum(number)
  ```

4. **wordsToCurrency**
  * <p>Accepts two arguments:
    <ul>
      <li>a number from 0 to 1 million in word form
      <li>any of 'USD', 'JPY' or 'PHP'
    </ul>
  </p>
  * <p>If the input currency doesn't match any of 'USD', 'JPY' or 'PHP' it returns 'unknown currency'<br/>
otherwise, it returns number in to its numerical form with a prefix of the currency</p>

  ######To call the function:
  ```
  numLib.wordsToNum(number, currency)
  ```
