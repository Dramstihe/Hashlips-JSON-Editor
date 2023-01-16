<body>
    <p>This script reads a list of names from a text file "names.txt" and uses them to update the "name" key of each element in a JSON file located at "PathTo/build/json/_metadata.json". It then writes the updated JSON to a new file "/new.json". The script uses the python built-in modules <code> json </code> and <code>random</code> .The script also makes sure that the same name is not used twice by keeping track of used names in a separate list and checking if it is empty before picking a random name from the names list. The script also indents the json file with 4 spaces for better readability.
    </p>
    <p> This script can be useful when you want to anonymize json files containing personal information, or when you want to randomly assign names to elements in a json file for any other use case. 
    </p>
</body>  
