function postData(input) {
    $.ajax({
        type: "POST",
        url: "/Test.py",
        data: { param: input },
        success: callback
    });
}

function callback(response) {
    console.log(response);
}

postData('data to process');