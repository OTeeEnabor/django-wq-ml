var currentTab = 0; // Current tab is set to be the first tab (0)
console.log(currentTab);
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form ...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    // ... and fix the Previous/Next buttons:
    if (n == 0) {
      document.getElementById("prevBtn").style.display = "none";
    } else {
      document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
      document.getElementById("nextBtn").innerHTML = "Submit";
      document.getElementById("nextBtn").type = 'submit'
    } else {
      document.getElementById("nextBtn").innerHTML = "Next";
    }
    // ... and run a function that displays the correct step indicator:
    fixStepIndicator(n)
}



function nextPrev(n) {
// get current tab
    var x = document.getElementsByClassName("tab")
    // click next button - n =1
    // validate current tab
    if (n==1 && !validateForm()) {
        return false;
    }
    x[currentTab].style.display = 'none';
    // increment current tab
    currentTab = currentTab + n;
    x[currentTab].display='block';

    // check if i have reached the end of form
    if (currentTab >= x.length) {
        // show submit button
        document.getElementById('').submit()
    } else{
        showTab(currentTab)
    }


}

function validateForm(){
    // define helper variables
    var x,y, i, valid = true;
    // get all the tabs
    x = document.getElementsByClassName("tab")
    // get the inputs in the current tab
    y = x[currentTab].getElementsByTagName("input");
    // loop through each field in the current input
    for (i=0;i <y.length; i++) {
        // if a field is empty or not a number
        if (y[i].value =="" || isNaN(y[i].value)){
            console.log(y[i].value)
            // add invalid class to the field
            y[i].className += " invalid "
            // add text to the field
            y[i].innerHTML = "Input is not valid. Please enter a number."
            valid = false;
        } else {
            // add invalid class to the field
            if (y[i].classList.contains(" invalid ")  )
            y[i].classNames -= " invalid "
            // add text to the field
            // y[i].innerHTML = "Input is not valid. Please enter a number."
            valid = true;
        }
    }
    return  valid;

}




function fixStepIndicator(n) {
// This function removes the "active" class of all steps...
var i, x = document.getElementsByClassName("step");
for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
}
//... and adds the "active" class to the current step:
x[n].className += " active";
}