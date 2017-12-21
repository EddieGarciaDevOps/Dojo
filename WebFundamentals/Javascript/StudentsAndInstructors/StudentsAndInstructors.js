var students = [ 
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
];

var users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
     ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
     ]
    };

students.forEach(function(entry) {
    console.log(entry.first_name, entry.last_name);
});

console.log("\n","Optional part:\n");

for (key in users) {
    var index = 0;
    console.log(key);
    users[key].forEach(function(entry) {
        index++;
        console.log(index, "-", entry.first_name, entry.last_name, "-", entry.first_name.length + entry.last_name.length);
    })
}