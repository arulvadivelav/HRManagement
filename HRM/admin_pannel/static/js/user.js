console.log("HERE")
function updateUserStatus(user_id, is_active){
    const url = "update_user_status/${user_id}"
    const data = {
        "is_active":is_active
    }
    fetch(
        url,{
            method:"PUT",
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify(data)
        }
    ).then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}