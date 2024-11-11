// Simulating a unique user identifier and joined rooms list for each session 
let userJoinedRooms = new Set(); // Set to track rooms the user has already joined

// Toggle Create Room Modal with visibility controls for the Available Study Rooms section and room list
function toggleCreateRoom() {
    const modal = document.getElementById("createRoomForm");
    const filterSection = document.querySelector(".filter-section");
    const roomList = document.getElementById("roomList");

    if (modal.style.display === "flex") {
        modal.style.display = "none";
        filterSection.style.display = "block";
        roomList.style.display = "flex";
    } else {
        modal.style.display = "flex";
        filterSection.style.display = "none";
        roomList.style.display = "none";
    }
}

// Add Event Listener to Create Room Form submission
document.getElementById("createRoom").addEventListener("submit", function (event) {
    event.preventDefault();
    const courseCode = document.getElementById("courseCode").value;
    const roomName = document.getElementById("roomName").value;
    const maxParticipants = document.getElementById("maxParticipants").value;
    const description = document.getElementById("description").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    addRoom(courseCode, roomName, maxParticipants, description, date, time);
    toggleCreateRoom();
});

// Array to hold study room objects
let studyRooms = [];

// Function to add a study room to the list
function addRoom(courseCode, roomName, maxParticipants, description, date, time) {
    const room = {
        courseCode,
        roomName,
        maxParticipants,
        description,
        date,
        time,
        currentParticipants: 0
    };
    studyRooms.push(room);
    displayRooms();
}

// Function to display all study rooms
function displayRooms() {
    const roomList = document.getElementById("roomList");
    roomList.innerHTML = "";
    studyRooms.forEach(room => {
        const roomItem = document.createElement("div");
        roomItem.classList.add("room-item");
        roomItem.innerHTML = `
            <h3>${room.roomName}</h3>
            <p>Course: ${room.courseCode}</p>
            <p>Participants: ${room.currentParticipants}/${room.maxParticipants}</p>
            <p>Description: ${room.description}</p>
            <p>Date: ${room.date}</p>
            <p>Time: ${room.time}</p>
            <button onclick="joinRoom('${room.roomName}')">Join Room</button>
        `;
        roomList.appendChild(roomItem);
    });
}

// Function to join a room with a pop-up confirmation
function joinRoom(roomName) {
    if (userJoinedRooms.has(roomName)) {
        showCenteredPopup(`You've already joined the room: ${roomName}`);
        return;
    }

    const room = studyRooms.find(r => r.roomName === roomName);
    if (room && room.currentParticipants < room.maxParticipants) {
        room.currentParticipants += 1;
        userJoinedRooms.add(roomName);
        displayRooms();
        showCenteredPopup(`You have successfully joined the room: ${roomName}`);
    } else {
        showCenteredPopup("Room is full or does not exist.");
    }
}

// Function to show a centered pop-up with a custom message
function showCenteredPopup(message) {
    const joinPopup = document.createElement("div");
    joinPopup.classList.add("join-popup");
    joinPopup.innerHTML = `<p>${message}</p>`;
    document.body.appendChild(joinPopup);

    setTimeout(() => {
        joinPopup.remove();
    }, 2000);
}

// Array to store forum posts and replies
let forumPosts = [];

// Function to add a new post to the forum
function addForumPost(content) {
    const post = {
        content,
        replies: [] // Array to store replies to this post
    };
    forumPosts.push(post);
    displayForumPosts();
}

// Function to display all forum posts and their replies
function displayForumPosts() {
    const forumPostsContainer = document.getElementById("forumPostsContainer");
    forumPostsContainer.innerHTML = ""; // Clear current display

    forumPosts.forEach((post, postIndex) => {
        const postContainer = document.createElement("div");
        postContainer.classList.add("forum-post");

        postContainer.innerHTML = `
            <p>${post.content}</p>
            <button onclick="showReplyInput(${postIndex})">Reply</button>
            <div class="replies">
                ${post.replies.map(reply => `<p class="reply">${reply}</p>`).join("")}
            </div>
            <div class="reply-input" id="reply-input-${postIndex}" style="display: none;">
                <input type="text" placeholder="Type your reply here" />
                <button onclick="addReply(${postIndex})">Post Reply</button>
            </div>
        `;

        forumPostsContainer.appendChild(postContainer);
    });
}

// Function to display the reply input for a specific post
function showReplyInput(postIndex) {
    const replyInput = document.getElementById(`reply-input-${postIndex}`);
    replyInput.style.display = replyInput.style.display === "none" ? "block" : "none";
}

// Function to add a reply to a specific post
function addReply(postIndex) {
    const replyInput = document.getElementById(`reply-input-${postIndex}`).querySelector("input");
    const replyText = replyInput.value.trim();

    if (replyText !== "") {
        forumPosts[postIndex].replies.push(replyText);
        replyInput.value = "";
        displayForumPosts();
    }
}

// Handle form submission for discussion forum posts
document.getElementById("forumPostForm").onsubmit = function(event) {
    event.preventDefault();
    const postContent = document.getElementById("forumPostContent").value;

    if (postContent.trim() !== "") {
        addForumPost(postContent);
        document.getElementById("forumPostContent").value = "";
    }
};
// Toggle Create Interest Group Modal
function toggleCreateInterestGroup() {
    const modal = document.getElementById("createInterestGroupForm");
    modal.style.display = modal.style.display === "flex" ? "none" : "flex";
}

// Array to hold interest-based groups
let interestGroups = [];

// Set to track groups the user has already joined
let joinedInterestGroups = new Set();  // Add this at the beginning of your JavaScript code

// Add Event Listener to Create Interest Group Form submission
document.getElementById("createInterestGroup").addEventListener("submit", function (event) {
    event.preventDefault();
    const interest = document.getElementById("interest").value;
    const description = document.getElementById("groupDescription").value;
    addInterestGroup(interest, description);
    toggleCreateInterestGroup(); // Close the modal
});

// Function to add an interest-based group
function addInterestGroup(interest, description) {
    const group = { interest, description, members: 0 };
    interestGroups.push(group);
    displayInterestGroups();
}

// Function to display all interest-based groups
function displayInterestGroups() {
    const interestGroupList = document.getElementById("interestGroupList");
    interestGroupList.innerHTML = ""; // Clear current display

    interestGroups.forEach((group, index) => {
        const groupItem = document.createElement("div");
        groupItem.classList.add("group-item");

        groupItem.innerHTML = `
            <h3>${group.interest}</h3>
            <p>${group.description}</p>
            <p>Members: ${group.members}</p>
            <button onclick="joinInterestGroup(${index})">Join Group</button>
        `;

        interestGroupList.appendChild(groupItem);
    });
}

// Function to join an interest-based group, preventing double joins
function joinInterestGroup(index) {
    const group = interestGroups[index];

    // Check if the user has already joined this group
    if (joinedInterestGroups.has(group.interest)) {
        showCenteredPopup(`You've already joined the group: ${group.interest}`);
        return;
    }

    group.members += 1; // Increase member count
    joinedInterestGroups.add(group.interest); // Mark the group as joined
    displayInterestGroups(); // Refresh the group display

    // Show confirmation message
    showCenteredPopup(`You have successfully joined the group: ${group.interest}`);
}

// Function to show a centered pop-up with a custom message
function showCenteredPopup(message) {
    const joinPopup = document.createElement("div");
    joinPopup.classList.add("join-popup");
    joinPopup.innerHTML = `<p>${message}</p>`;
    document.body.appendChild(joinPopup);

    // Automatically remove the pop-up after 2 seconds
    setTimeout(() => {
        joinPopup.remove();
    }, 2000);
}
