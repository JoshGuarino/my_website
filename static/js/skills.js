const data = [{section: "Programming Languages", content: ["C/C++", "Python", "Javascript(node.js)", "PHP", "HTML", "CSS"], info: ""}, 
              {section: "Frameworks & Libraries", content: ["Bootstrap", "JQuery", "react.js", "vue.js", "express.js", "flask", "django", "laravel"], info: ""}, 
              {section: "Package Managers", content: ["npm", "pip", "composer"], info: ""}, 
              {section: "Database Software", content:["MS SQL Server", "MySql", "MongoDB", "PostgreSQL"], info: ""}, 
              {section: "Version Control w/ GIT", content: ["gitlab", "github"], info: ""}, 
              {section: "Software Testing/QA", content: ["selenium", "sikuli", "regression", "performance"], info: ""}];

const populateModal = (arr_pos) =>{
    $('#m_content').html('');
    $('#m_title').html('');
    $('#m_title').html(data[arr_pos].section);
    data[arr_pos].content.forEach(element => {
        $('#m_content').append('<li>' + element + '</li>');
    });
};
