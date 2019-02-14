const data = [{section: "Programming Languages", info: "C/C++, Python, Javascript(node.js), PHP, HTML, CSS"}, 
              {section: "Frameworks & Libraries", info: "Bootstrap, JQuery, react.js, vue.js, express.js, flask, django"}, 
              {section: "Package Managers", info: "npm, pip"}, 
              {section: "Database Software", info: "MS SQL Server, MySql, MongoDB, PostgreSQL"}, 
              {section: "Version Control w/ GIT", info: "gitlab, github"}, 
              {section: "Software Testing/QA", info: "automation(selenium, sikuli), regression, performance"}];

const populateModal = (arr_pos) =>{
    $('#m_title').html(data[arr_pos].section);
    $('#m_content').html(data[arr_pos].info);
}
