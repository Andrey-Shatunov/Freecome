import React from 'react'
import AddingFrom from './Stateless/AddingForm'

export default class Income extends React.Component {
	
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div className="row">
				<div className="col-4">
					<div className="card">
						<h5 className="card-header">Incomes</h5>
						<div className="card-block">
							<AddingFrom />	
						</div>
					</div>
				</div>
				<div className="col-8">
					<table className="table table-hover">
						<thead>
							<tr>
								<td>Date</td>
								<td>Description</td>
								<td>Amount</td>
								<td></td>
								<td></td>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>22.05.2016</td>
								<td>Food</td>
								<td>1200₽</td>
								<td></td>
								<td>
									<button type="button" className="close" aria-label="Close">
									  <span aria-hidden="true">&times;</span>
									</button>
								</td>
							</tr>
						</tbody>
					</table>	
				</div>
			</div>			
		)
	}

}
