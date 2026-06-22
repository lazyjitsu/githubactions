## This is the python app


#### Create the basic directory/file structure for this simple demo
```
mkdir src
touch src/__init__.py # for importing/exporting packages
mkdir tests  #pytest needs this
```
Our structure now looks like this thanks to the tree command:
```
tree .
Folder PATH listing for volume LENOVO
Volume serial number is 00000057 0CBC:E19B
D:\MYSOURCE\TRAINING\MLOPS\UDEMY\COMPLETEMLOPS-BOOTCAMP\INTROGITHUBACTIONS
├───src
└───tests
```
The most basic of tests is ou source (the two functions in math_operations) and the tests folder which must exist and test_operations assert code.
<style>
    /* The Flexbox Parent Container */
    .code-row {
      display: flex;
      flex-direction: row;      /* Places columns horizontally */
      gap: 16px;                /* Adds spacing between the two columns */
      width: 100%;
      box-sizing: border-box;
    }
    /* The Flexbox Child Items (Columns) */
    .code-column {
      flex: 1;                  /* Distributes space equally (50% width each) */
      min-width: 0;             /* Crucial: prevents long code lines from breaking layout */
    }
    /* Styling for the actual pre/code containers */
    pre {
      background-color: #2d3748; /* Dark mode background color */
      color: #f7fafc;           /* Light text color */
      padding: 16px;
      border-radius: 8px;
      margin: 0;
      overflow-x: auto;         /* Adds horizontal scrollbars if lines are too long */
    }
    code {
      font-family: 'Courier New', Courier, monospace;
    }
</style>
  <div class="code-row">
    <div class="code-column">
        <pre><code>
    // <font style='color:white'> file: src/math_operations.py </font><br>
            def add(a,b):
                return a+b
            def subtract(a,b):
                return a-b
        </pre></code>
    </div>
    <div class="code-column">
    <pre><code>
        // <font style='color:white'> file: tests/test_operations.py </font><br>
        def test_add():
            assert add(2,3)==5
            assert add(1,2)==3
            assert add(4,5)==9
        def test_subtract():
            assert subtract(3,1)==1
            assert subtract(1,4)==-3
            assert subtract(5,2)==3
            assert subtract(10,2)==8
    </pre></code>
    </div>
 </div>


Now go to github actions after creating your github repo. In our case our repo is called 'githubactions'  Probably should have called it something else cause it sounds too much like it was githubs creation but it's the repo i created.

Lets make the github actions folder
```
mkdir -p .github/workflows
# lets create a file, we'll call it unittest.yml
touch .github/workflows/unittest.yml

```
