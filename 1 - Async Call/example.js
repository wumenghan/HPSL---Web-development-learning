import React from 'react';

/**
 * Check whether you run this app on server or local.
 * If it is on server, you need to add a prefix 
 */
const host = window.location.host;
var prefix = '';
if (host === 'crowd.ecn.purdue.edu') {
    prefix = '/10';  // Change this to your port number. 
} 
window.prefix = prefix; // window is a global object, you can access it across all the js files you include in the html file. 


class Example extends.React.Component {
	constructor(props) {
		this.state = {
			buttons: [
				{id: "btn_1"},
				{id: "btn_2"},
			],
			content: ""
		}
		this.onPressButton = this.onPressButton.bind(this);
	}

	onPressButton(evt) {
		buttonId = evt.target.id; // Get the button id

		data = {
			buttonId: buttonId
		}

		// Fire an async call to server, get the required data and update the UI.
		fetch(window.prefix + '/get_mturk_data', {
			method: 'POST',
			body: JSON.stringify(data), // Conver the data object to string.
			headers: {
				'Accept': 'application/json',
	          	'Content-Type': 'application/json'
			},
		}).then(res => res.json()) // Convert the JSON string to object
		.then(
			(res) => { // Now res is an object. We update the state using setState.
				this.setState({
					content: res.content;
				})
			}
		)
	}

	render() {
		const buttons = this.state.buttons;
		const content = this.state.content;
		return (
			<div>
				<h1>Async call examples</h1>
				{buttons.map((button, index) => {
					return (
					<button
						id={button.id}
						key={index}
						data={button}
						onClick={this.onPressButton} 
					/>
					)
				})}
				<div>
					{content}
				</div>
			</div>
			);
	}
}

export default Example;