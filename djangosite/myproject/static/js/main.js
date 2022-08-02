

const spinnerBox = document.getElementById('spinner-box');
const dataBox = document.getElementById('data-box');

// console.log(spinnerBox);
// console.log(dataBox);

$.ajax({
    type: 'GET',
    url: '/https://hotelapi.loyalty.dev/api/hotels/diH7/price?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1/',
    success: function(response){
        setTimeout(()=>{
            spinnerBox.classList.add('not-visible')
            for (const item of response){
                dataBox.innerHTML += `<b>$(item.title)</b>`
            }
        },1000)
        spinnerBox.classList.add('not-visible')
        console.log('response', response)
    },
    error: function(error){
        console.log(error)
    }
})