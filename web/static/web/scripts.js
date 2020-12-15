console.log('js')

function run_view() {
    console.log('rv');
    ReactDOM.render(<ImagesLoader/>, document.querySelector('#images'))
}

class ImagesLoader extends React.Component {
    constructor(props) {
        console.log('loader'),
        super(props);
        this.state = {
            images: [{}],
            isDataFetched: false
        };
        this.fetchPage(1);
    };
    fetchPage(page_id) {
        fetch(`api/images`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then(result => {
            this.setState({
                images: result,
                isDataFetched: true
            })
        })
    };
    render() {
        if(!this.state.isDataFetched) return null;
        return(
            <div>
                <Images images={this.state.images} />
            </div>
        )
    }
};

class Images extends React.Component {
    render() {
        let feed = [];
        for (let i = 0; i < this.props.images.length; i++) {
            feed.push(<Image key={i} image={this.props.images[i]}/>)
        }
        return(

            <div>
                <div className="tile is-ancestor">
                    
                    {feed}
                    
                </div>
            </div>
        )
    }
}

class Image extends React.Component {
    constructor(props) {
        super(props);
        console.log("props");
        console.log(props);
        this.state = {
            title: this.props.image.title,
            content: this.props.image.content,
            image: this.props.image.image,
            user: this.props.image.user,
            timestamp: new Date(this.props.image.timestamp)
        }
    };
    render () {
        return(
            <div className="tile is-parent">
                <div class="card">
                <div class="card-image">
                    <figure class="image is-4by3">
                        <img src={this.state.image}/>
                    </figure>
                </div>
                <div class="card-content">
                    <div class="media">
                    <div class="media-left">
                        <figure class="image is-48x48">
                        <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image" />
                        </figure>
                    </div>
                    <div class="media-content">
                        <p class="title is-4">{this.state.title}</p>
                        <p class="subtitle is-6">@{this.state.user.username}</p>
                    </div>
                    </div>

                    <div class="content">
                    {this.state.content}
                    <br />
                    {this.state.timestamp.toLocaleString()}
                    </div>
                </div>
                </div>
            </div>
        )
    }
}

run_view();