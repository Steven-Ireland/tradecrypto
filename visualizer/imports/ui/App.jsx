import React, { Component } from 'react';
import { Votes } from '../api/votes.js';
import { createContainer } from 'meteor/react-meteor-data';

// App component - represents the whole app
class App extends Component {
  render() {
    return <div>{this.renderVotes()}</div>
  }
  renderVotes() {
    return this.props.votes.map((vote) => (
      <p>{vote.user}, {vote.from}, {vote.to}</p>
    )); 
  }
}

export default createContainer(() => {
  return {
    votes: Votes.find({}).fetch(),
  };
}, App);
