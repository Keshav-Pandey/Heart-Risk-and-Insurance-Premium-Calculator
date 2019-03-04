var hypertension;
var heart_disease;
var work_type;
var smoking_status;
var avg_glucose_level;
var Residence_type;
var married;
var gender;
var ans;

function hyper(val){
    hypertension = val;
    if(hypertension){
        var target = $("#married");
        $('html, body').animate({
            scrollTop: (target.offset().top - 72)
          }, 1000, "easeInOutExpo");
    }
    else{
        var target = $("#heart");
        $('html, body').animate({
            scrollTop: (target.offset().top - 72)
          }, 1000, "easeInOutExpo");
    }
}

function heart(val){
    heart_disease = val;
    if(hypertension == false && heart_disease == false){
        var target = $("#work");
        $('html, body').animate({
            scrollTop: (target.offset().top - 72)
          }, 1000, "easeInOutExpo");
    } else if(hypertension == true && married == false && work_type == true){
        if(heart_disease){
            var target = $("#gender");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
            }, 1000, "easeInOutExpo");
        } else {
            var target = $("#residence");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
            }, 1000, "easeInOutExpo");
        }
    } else if(hypertension == true && married == true) {
        if(heart_disease)
            ans = 5;
        else
            ans = 4;
        gotoResults();
    }
}

function work(val){
    work_type = val;
    if(hypertension == false && heart_disease == false){
        if(work_type == false){
            var target = $("#smoke");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        } else {
            var target = $("#married");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        }
    } else if(hypertension == false && heart_disease == true){
        if(work_type == false) {
            ans = 2;
            gotoResults();
        } else {
            var target = $("#residence");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        }
    } else if(hypertension == true && married == false){
        if(work_type == false) {
            var target = $("#gender");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        } else {
            var target = $("#heart");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        }
    }
}

function smoke(val){
    smoking_status = val;
    if(hypertension == false && heart_disease == false && work_type == false){
        if(smoking_status == true) {
            var target = $("#glucose");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        } else {
            var target = $("#residence");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        }
    }
}

function glucose(val){
    avg_glucose_level = val;
    if(hypertension == false && heart_disease == false && work_type == false && smoking_status == true){
        if(avg_glucose_level == false)
            ans = 2;
        else 
            ans = 1;
        gotoResults();
    }
}

function res(val){
    Residence_type = val;
    if(hypertension == false && heart_disease == false && work_type == false && smoking_status == false){
        ans = 1;
        gotoResults();
    } else if(hypertension == false && heart_disease == true && work_type == true){
        ans = 4;
        gotoResults();
    } else if(hypertension == true && married == false && work_type == true && heart_disease == false){
        if(Residence_type == false)
            ans = 3;
        else
            ans = 4;
        gotoResults();
    } else if(hypertension == true && married == true){
        var target = $("#heart");
        $('html, body').animate({
            scrollTop: (target.offset().top - 72)
            }, 1000, "easeInOutExpo");
    }
}

function marr(val){
    married = val;
    if(hypertension == false && heart_disease == false && work_type == true){
        ans = 2;
        gotoResults();

    } else if(hypertension == true){
        if(married == false){
            var target = $("#work");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        } else {
            var target = $("#residence");
            $('html, body').animate({
                scrollTop: (target.offset().top - 72)
              }, 1000, "easeInOutExpo");
        }
    }
}

function gender(val){
    gender = val;
    if(hypertension == true && married == false && work_type == false){
        if(gender)
            ans = 1;
        else
            ans = 2;
        gotoResults();            
    } else if(hypertension == true && married == false && work_type == true && heart_disease == true){
        if(gender)
            ans = 4;
        else
            ans = 5;
        gotoResults();
    }
}

function gotoResults(){
    draw();
    var target = $("#results");
    $('html, body').animate({
        scrollTop: (target.offset().top - 72)
      }, 1000, "easeInOutExpo");
}

function draw(){
    var opts = {
        angle: -0.2, // The span of the gauge arc
        lineWidth: 0.2, // The line thickness
        radiusScale: 1, // Relative radius
        pointer: {
          length: 0.6, // // Relative to gauge radius
          strokeWidth: 0.035, // The thickness
          color: '#000000' // Fill color
        },
        limitMax: false,     // If false, max value increases automatically if value > maxValue
        limitMin: false,     // If true, the min value of the gauge will be fixed
        strokeColor: '#E0E0E0',  // to see which ones work best for you
        generateGradient: true,
        highDpiSupport: true,     // High resolution support
        staticLabels: {
            font: "25px sans-serif",  // Specifies font
            labels: [0, 1, 2, 3, 4, 5],  // Print labels at these values
            color: "#000000",  // Optional: Label text color
            fractionDigits: 0  // Optional: Numerical precision. 0=round off.
          },
          staticZones: [
            {strokeStyle: "#F03E3E", min: 4, max: 5}, // Red from 100 to 130
            {strokeStyle: "#FFDD00", min: 3, max: 4}, // Yellow
            {strokeStyle: "#30B32D", min: 2, max: 3}, // Green
            {strokeStyle: "#FFDD00", min: 1, max: 2}, // Yellow
            {strokeStyle: "#F03E3E", min: 0, max: 1}  // Red
         ],
        
      };
      var target = document.getElementById('graph'); // your canvas element
      var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
      gauge.maxValue = 5; // set max gauge value
      gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
      gauge.animationSpeed = 32; // set animation speed (32 is default value)
      gauge.set(ans); // set actual value
}