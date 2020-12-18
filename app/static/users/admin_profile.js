$(function () {
    // TODO:
    // open modal on clicking more details
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
                    `<h6>${element.split("-")[0]} X ${element.split("-")[1]}</h6>`
                )
            }
        })
    })

    $(".close").on("click", function () {
        $(".modal").hide()
    })

    $(".markAsCompleted").on("click", function () {
        $("#complete").show()
        $(".delete").attr("data-id", $(this).data("id"))
    })

    $(".delete").on("click", function () {
        let id = $(this).data("id")
        let getUrl = window.location
        window.location.replace(
            `${getUrl.protocol + "//" + getUrl.host + "/"}deleteOrder/${id}`
        )
        $(".modal").hide()
    })
})