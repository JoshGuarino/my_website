$(function(){

    $("#page_link_home").mouseover(function(){
        $('#icon_home').toggle();
        $('#text_home').toggle();
    }).mouseout(function(){
        $('#icon_home').toggle();
        $('#text_home').toggle();
    });
    $("#page_link_about").mouseover(function(){
        $('#icon_about').toggle();
        $('#text_about').toggle();
    }).mouseout(function(){
        $('#icon_about').toggle();
        $('#text_about').toggle();
    });

    $("#page_link_skills").mouseover(function(){
        $('#icon_skills').toggle();
        $('#text_skills').toggle();
    }).mouseout(function(){
        $('#icon_skills').toggle();
        $('#text_skills').toggle();
    });

    $("#page_link_contact").mouseover(function(){
        $('#icon_contact').toggle();
        $('#text_contact').toggle();
    }).mouseout(function(){
        $('#icon_contact').toggle();
        $('#text_contact').toggle();
    });

});
