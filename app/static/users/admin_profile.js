$(function () {
    // TODO: open modal on clicking more details
    $(".more").on("click", function () {
        $("#myModal").show()
        $(".modal-body").html("")
        let details = $(this).data("details")
        details.split(", ").forEach((element) => {
            if (
                element.split("-")[0] == undefined ||
                element.split("-")[1] == undefined
            ) {
            } else {
                $(".modal-body").append(
                    <h6>${element.split("-")[0]} X ${element.split("-")[1]}</h6>
                )
            }
        })
    })

    $(".close").on("click", function () {
        $("#myModal").hide()
    })
})