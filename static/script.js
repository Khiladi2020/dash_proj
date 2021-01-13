function showLoader(){
    $(".loader_container").addClass("loader");
}

function hideLoader(){
    $(".loader_container").removeClass("loader");
}
function rmColor(card,cls){
    card.find(".card-header").removeClass(cls);
    card.find(".card-body").removeClass(cls);
}
function addColor(card,cls){
    card.find(".card-header").addClass(cls);
    card.find(".card-body").addClass(cls);
}

function fetch_status(){
    var safe = 0;
    var unsafe = 0;
    $.ajax({
        type: 'GET',
        url: "http://127.0.0.1:5000/get_data_current",
        beforeSend: function(){
            showLoader(); //show loader
        },
        success: function(data, status){
            //console.log(status,data);
            for (container of data){
                var card = $("#"+container.id);
                card.find(".status").text(container.status);
                card.find(".curr_temp").html(container.current_temp + " &#8451;");
                card.find(".safe_temp_range").html(container.safe_range + " &#8451;");
                if (container.status === "UnSafe"){
                    unsafe++;
                    addColor(card,"danger_col");
                    rmColor(card,"warning_col");
                }
                else if(container.status === "Alert!"){
                    addColor(card,"warning_col");
                }
                else{
                    safe++;
                    rmColor(card,"danger_col");
                    //removing warning classes
                    rmColor(card,"warning_col");

                }
            }
            $("#safe_stat").text(safe);
            $("#safe_stat").data("stat_val",safe);
            $("#unsafe_stat").text(unsafe);
            $("#unsafe_stat").data("stat_val",unsafe);
        },
        complete: function(data){
            setTimeout(hideLoader,1000);
        }
    });
}

function alert_creator(msg){
    data = '<div class="alert alert-warning alert-dismissible fade show" role="alert" > ' +
        msg + 
        '<button type="button" class="close" data-dismiss="alert" aria-label="Close"> \
        <span aria-hidden="true">&times;</span> \
        </button> \
        </div>'
    //console.log(data);
    $("#alert_container").html(data);
}

function send_data_server(send_url,formData,alert){
    $.ajax({
        type: 'POST',
        url: send_url,
        data: formData,
        success: function(data, status){
            console.log(data,status);
            if(alert === 1){
                alert_creator(data);
            }
        },
        error: function() {
            if(alert === 1){
                alert_creator("Some Error Occured!");
            }
        }
    });
}

$(document).ready(function(){
    //enabling tooltips
    $('[data-toggle="tooltip"]').tooltip()

    //for load on click refresh
    $("#load").click(function(){
        fetch_status();
    });
    //loading data for first time
    fetch_status();

    //refreshing after every few seconds
    setInterval(fetch_status,5000);

    //beer data send
    $("#createBear_Form").submit(function(event) {
        console.log(" create beer submit ");
        event.preventDefault();
        var formData = {
            "b_name": $("#beer").val(),
            "b_min_tmp": $("#beer_min").val(),
            "b_max_tmp": $("#beer_max").val()
        };

        var send_url = "/create_new_beer";
        send_data_server(send_url,formData,1);
        $('#BeerModal').modal("hide");
    });

    //container data send
    $("#createCont_Form").submit(function(event) {
        console.log(" create container submit ");
        event.preventDefault();
        var formData = {
            "c_name": $("#cont_name").val(),
            "b_id": $("#cont_beer_type").val(),
            "b_type": $("#cont_beer_type option:selected").text()
        };

        var send_url = "/create_new_container";
        send_data_server(send_url,formData,1);
        $('#ContainerModal').modal("hide");
    });

});