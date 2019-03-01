const data = [{section: "Programming Languages", content: ["C/C++", "Python", "Javascript(node.js)", "PHP", "HTML", "CSS"], 
               info: "I am proficient in the languages I have listed, with python and JS being what I have the higest skill level in. I am in the process of learning C#, java, and GO."}, 
              {section: "Frameworks & Libraries", content: ["Bootstrap", "Materialize", "JQuery", "react.js", "Vue.js", "express.js", "Flask", "Django", "Laravel"], 
               info: "These are the frameoworks I have used or are proficient in. This site is being built using Flask, Bootstrap, JQuery, and Jinga2. I am also learning the .NET framework and improving my vue and react skills."}, 
              {section: "Package Managers", content: ["npm", "pip", "composer"], 
               info: "These are the package mangers I have used the most. NPM for javascript, PIP for python, and composer for PHP. "}, 
              {section: "Database Software", content:["MS SQL Server", "MySql", "MongoDB", "PostgreSQL"], 
               info: "I have used numerous DB software, with SQL databases being a majority of my experience. I have no-sql DB experience in MongoDB and I am continuing to improve my skills in that area."}, 
              {section: "Version Control w/ GIT", content: ["gitlab", "github"], 
               info: "All my version control experience comes from using GIT. I use github for my personal projects. I have used both gitlab and github for development and testing jobs."}, 
              {section: "Software Testing/QA", content: ["selenium", "sikuli", "regression", "performance"], 
               info: "I have had numerous testing experience. I have done regression and performance testing manually.  I have also done automated testing using selenium and sikuli."}];

const populateModal = (arr_pos) =>{
    $('#m_content').html('');
    $('#m_title').html('');
    $('#m_title').html(data[arr_pos].section);
    data[arr_pos].content.forEach(element => {
        $('#m_content').append('<li>' + element + '</li>');
    });
    $('#m_info').html(data[arr_pos].info);
};
