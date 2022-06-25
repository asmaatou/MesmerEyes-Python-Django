$(document).ready(function(){
    SaveForm = function(){
        //dataform = form.serialize();
        var formData  = new FormData(this);
        $.ajax({
            url: $(this).attr("data-url"),
            type: $(this).attr("method"),
            data     : formData,
            processData:false,
            contentType:false,
            dataType: 'json',
            success: function(data){
                $('.show-form').trigger("reset");
            },
        });
    
    };

////////////////////////////////////////////////////////////////////////////////////////////////////

    ShowForm_cat = function(){
        btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: $(this).attr("method"),
            dataType:'json',
            beforeSend: function(){
                $('#modal-cat').modal('show');
            },
            success: function(data){
                $('#modal-cat .modal-content').html(data.html_form);
            }
        });
    };

     $(".show-form").click(ShowForm_cat);
     $("#modal-cat").on("submit",".create-form",SaveForm);

     $('#cat-table').on("click",".show-form-update",ShowForm_cat);
     $('#modal-cat').on("submit",".update-form",SaveForm);

     $('#cat-table').on("click",".show-form-delete",ShowForm_cat);
     $('#modal-cat').on("submit",".delete-form",SaveForm);
////////////////////////////////////////////////////////////////////////////////////////////////////

    ShowForm_prod = function(){
        btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: $(this).attr("method"),
            dataType:'json',
            beforeSend: function(){
                $('#modal-prod').modal('show');
            },
            success: function(data){
                $('#modal-prod .modal-content').html(data.html_form);
            }
        });
    };

     $(".show-form").click(ShowForm_prod);
     $("#modal-prod").on("submit",".create-form",SaveForm);

     $('#prod-table').on("click",".show-form-update",ShowForm_prod);
     $('#modal-prod').on("submit",".update-form",SaveForm);

     $('#prod-table').on("click",".show-form-delete",ShowForm_prod);
     $('#modal-prod').on("submit",".delete-form",SaveForm);

////////////////////////////////////////////////////////////////////////////////////////////////////////

    ShowForm_gam = function(){
        btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'GET',
            dataType:'json',
            beforeSend: function(){
                $('#modal-gam').modal('show');
            },
            success: function(data){
                $('#modal-gam .modal-content').html(data.html_form);
                
            }
        });
    };

    $(".show-form").click(ShowForm_gam);
    $("#modal-gam").on("submit",".create-form",SaveForm);

    $('#gam-table').on("click",".show-form-update",ShowForm_gam);
    $('#modal-gam').on("submit",".update-form",SaveForm);

    $('#gam-table').on("click",".show-form-delete",ShowForm_gam);
    $('#modal-gam').on("submit",".delete-form",SaveForm);



////////////////////////////////////////////////////////////////////////////////////////////////////////


     ShowForm_image = function(){
        btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'GET',
            dataType:'json',
            beforeSend: function(){
                $('#modal-img').modal('show');
            },
            success: function(data){
                $('#modal-img .modal-content').html(data.html_form);
            }
        });
    };

    

    $(".show-form").click(ShowForm_image);

    $("#modal-img").on("submit",".create-form",SaveForm);

    $('#img-table').on("click",".show-form-update",ShowForm_image);
    $('#modal-img').on("submit",".update-form",SaveForm);

    $('#img-table').on("click",".show-form-delete",ShowForm_image);
    $('#modal-img').on("submit",".delete-form",SaveForm);
////////////////////////////////////////////////////////////////////////////////////////////////////////

    ShowForm_admin= function(){
        btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'GET',
            dataType:'json',
            beforeSend: function(){
                $('#modal-a').modal('show');
            },
            success: function(data){
                $('#modal-a .modal-content').html(data.html_form);
                
            }
        });
    };

    $('#admin-table').on("click",".show-form-update",ShowForm_admin);
    $('#modal-a').on("submit",".update-form",SaveForm);

    $('#admin-table').on("click",".show-form-delete",ShowForm_admin);
    $('#modal-a').on("submit",".delete-form",SaveForm);



});