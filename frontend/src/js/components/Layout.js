import React from 'react'

export default (props) => {

    return (
        <div>
	        <nav className="navbar navbar-toggleable-md navbar-light bg-faded" style={{"margin-bottom": "3em"}}>
				<div className="container">
					<button className="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				    	<span className="navbar-toggler-icon"></span>
				  	</button>
				  	<a className="navbar-brand" href="/dashboard">Freecome</a>
					<div className="collapse navbar-collapse" id="navbarSupportedContent">
				    	<ul className="navbar-nav mr-auto">
				     		<li className="nav-item active">
				        		<a className="nav-link" href="/dashboard/income">Income</a>
				      		</li>
				      		<li className="nav-item">
				        		<a className="nav-link" href="/dashboard/expenditure">Expenditure</a>
				      		</li>
				    	</ul>
				  	</div>
				</div>
			</nav>
			
			<div className="container">
				{ props.children }
			</div>
        </div>
    );

}

