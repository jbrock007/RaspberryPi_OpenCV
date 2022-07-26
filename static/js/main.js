/**
 * Updates the current shape, distance and motor status calling
 * the corresponding methods.
 */
function updateStatus() {
    // Update current shape based on Open CV
    (async () => await updateCurrentShapeOpenCV())();
    // Update motor status
    (async () => await updateMotorStatus())();
    // Update current shape based on Distance
    (async () => await updateCurrentShapeDistance())();
    // Update current distance
    (async () => await updateDistance())();
}

/**
 * Update the current shape based on OpenCV.
 */
async function updateCurrentShapeOpenCV() {
    try {
        // Request shape from server
        const requestResult = await requestShapeFromOpenCV()
        console.log("Shape from opencv :" + requestResult.data)
        // Get the HTML element where the status is displayed
        const triangle_open_cv = document.getElementById('triangle_open_cv')
        triangle_open_cv.innerHTML = requestResult.data[0]
        const square_open_cv = document.getElementById('square_open_cv')
        square_open_cv.innerHTML = requestResult.data[1]
        const circle_open_cv = document.getElementById('circle_open_cv')
        circle_open_cv.innerHTML = requestResult.data[2]
    } catch (e) {
        console.log('Error getting the shape based on OpenCV', e)
        updateStatus('Error getting the shape based on OpenCV')
    }
}

/**
 * Function to request the server to update the current
 * shape based on OpenCV.
 */
function requestShapeFromOpenCV() {
    try {
        // Make request to server
        return axios.get('/get_shape_from_opencv')
    } catch (e) {
        console.log('Error getting the status', e)
        updateStatus('Error getting the status')
    }
}


/**
 * Function to request the server to start the motor.
 */
function requestStartMotor() {
    try {
        // Make request to server
        return axios.get('/start_motor')
        // (async () => await updateMotorStatus())();
    } catch (e) {
        console.log('Error starting the Motor', e)
        updateStatus('Error starting the Motor')

    }
}

/**
 * Function to request the server to stop the motor.
 */
function requestStopMotor() {
    try {
        axios.get('/stop_motor')
        // (async () => await updateMotorStatus())();
    } catch (e) {
        console.log('Error starting the Motor', e)
        updateStatus('Error starting the Motor')

    }
}

function requestMotorStatus() {
    try {
        // Make request to server
        return axios.get('/motor_status')
    } catch (e) {
        console.log('Error starting the Motor', e)
        updateStatus('Error starting the Motor')
    }
}
/**
 * Update the status of the motor.
 * @param {String} status
 */
async function updateMotorStatus(status) {
    try{
        // Get the HTML element where the status is displayed       
        const requestResult = await requestMotorStatus()
        console.log("Motor start Status :" + requestResult.data)
        const motor_status = document.getElementById("motor_status")    
        if (requestResult.data[0] === true){
            motor_status.innerHTML = requestResult.data[1]
        }
        else {
            motor_status.innerHTML = "Motor is stopped"
        }
    }catch (e) {
        console.log('Error getting the Motor status', e)
        updateStatus('Error getting the Motor status')

    }
}

/**
 * Update the current shape based on distance sensor.
 */
async function updateDistance() {
    // Get the HTML element where the status is displayed
    const distance = await requestDistance()
    console.log("Distance :" + distance.data)
    const shape_distance = document.getElementById('shape_distance')
    shape_distance.innerHTML = distance.data
}


/**
 * Function to request the server to get the distance from
 * the rod to the ultrasonic sensor.
 */
function requestDistance() {
    try {
        // Make request to server
        return axios.get('/get_distance')
    } catch (e) {
        console.log('Error getting the status', e)
        updateStatus('Error getting the status')
    }
}

/**
 * Update the current shape based on distance sensor.
 */
async function updateCurrentShapeDistance() {
    // Get the HTML element where the status is displayed
    try {
        // Request shape from server
        const requestShapeDistance = await requestShapeFromDistance()
        console.log("Shape from Distance :" + requestShapeDistance.data)
        // Get the HTML element where the status is displayed
        const triangle_from_distance = document.getElementById('triangle_from_distance')
        triangle_from_distance.innerHTML = requestShapeDistance.data[0]
        const square_from_distance = document.getElementById('square_from_distance')
        square_from_distance.innerHTML = requestShapeDistance.data[1]
        const circle_from_distance = document.getElementById('circle_from_distance')
        circle_from_distance.innerHTML = requestShapeDistance.data[2]
    } catch (e) {
        console.log('Error getting the shape based on OpenCV', e)
        updateStatus('Error getting the shape based on OpenCV')
    }

}

/**
 * Function to request the server to get the shape based
 * on distance only.
 */
function requestShapeFromDistance() {
    try {
        // Make request to server
        return axios.get('/get_shape_from_distance')
    } catch (e) {
        console.log('Error getting the status', e)
        updateStatus('Error getting the status')
    }
}
