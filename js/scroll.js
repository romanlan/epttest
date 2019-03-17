var navloaction = document.getElementById("top-rate");
var height=navloaction.offsetTop;
document.documentElement.scrollTop=height;

var timer=setInterval(function()
{
    var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;
    console.log(scrollTop);
    var ispeed=10;
    if(scrollTop>1000)
    {
        clearInterval(timer);
    }
    document.documentElement.scrollTop=document.body.scrollTop=scrollTop+ispeed;
},30)
