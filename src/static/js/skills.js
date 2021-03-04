const populateModal = (repo) =>{
    data = document.querySelector(`#${repo}`);
    document.getElementById('m_title').innerHTML = repo;
    document.getElementById('m_info').innerHTML = data.dataset.description;
    document.getElementById('url').href = data.dataset.url;
    
};
