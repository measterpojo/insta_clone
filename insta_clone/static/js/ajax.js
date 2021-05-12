




const likeunlikeforms = document.querySelectorAll('.likebtn');
const likeunlikebtn = document.getElementsByClassName('btn-value')

for (i = 0; i < likeunlikebtn.length; i++){
    likeunlikebtn[i].addEventListener('click', function(){
        var href = this.dataset.value
        console.log(href)

        likeunlikeforms.forEach(el =>{
            el.addEventListener('click', (e)=>{
                
                e.preventDefault()      

                $.ajax({
                    type: 'GET',
                    url : href + '/like',
                
                    success: function(response){
                        window.location.reload(true);
                        console.log(response)
                    },
                    error: function(error){
                        console.log(error)
                    }

                })

            });
        });



})
}


