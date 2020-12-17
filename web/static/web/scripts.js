console.log('js')

document.querySelector('#home-btn').addEventListener('click', () => view_home());

function view_home() {
    console.log('home');
    document.querySelector('#home').style.display = 'block';
    document.querySelector('#detail').style.display = 'none';
    ReactDOM.render(<ImagesLoader/>, document.querySelector('#home'))
}
function image_detail(id) {
    console.log(id)
    document.querySelector('#home').style.display = 'none';
    document.querySelector('#detail').style.display = 'block';
    ReactDOM.render(<ImageDetail id={id}/>, document.querySelector('#detail'))
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

class ImageDetail extends React.Component {
    constructor(props) {
        super(props);
        console.log(this.state);
        this.state = {
            image: {},
            isDataFetched: false
        };
        this.fetchImage(this.props.id)
    };
    fetchImage(id) {
        fetch(`api/images/${id}`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then(result => {
            this.setState({
                image: result,
                isDataFetched: true
            })
        })
    };
    render() {
        if(!this.state.isDataFetched) return null;
        return(
            <div>
                <Image image={this.state.image}/>
            </div>
        )
    }
}

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
            id: this.props.image.id,
            title: this.props.image.title,
            content: this.props.image.content,
            image: this.props.image.image,
            user: this.props.image.user,
            tags: this.props.image.tags,
            timestamp: new Date(this.props.image.timestamp)
        };
        console.log(this.state.id)
    };
    detail = () => {
        console.log("detail");
        image_detail(this.state.id);
    };
    render() {
        return(
            <div className="tile is-parent">
                <a className="card" onClick={this.detail}>
                    <div className="card-image">
                        <figure className="image is-4by3">
                            <img src={this.state.image}/>
                        </figure>
                    </div>
                    <div className="card-content">
                        <div className="media">
                        <div className="media-left">
                            <figure className="image is-48x48">
                            <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image" />
                            </figure>
                        </div>
                        <div className="media-content">
                            <p className="title is-4">{this.state.title}</p>
                            <p className="subtitle is-6">@{this.state.user.username}</p>
                        </div>
                        </div>
                        <div className="content">
                        {this.state.content}
                        <br />
                        {this.state.timestamp.toLocaleString()}
                        <br />
                        <Tags tags={this.state.tags} />
                        </div>
                    </div>
                </a>
            </div>
        )
    }
}

class Tags extends React.Component {
    render () {
        let feed = [];
        for (let i = 0; i < this.props.tags.length; i++) {
            feed.push(<Tag key={i} tag={this.props.tags[i]} />)
        }
        return(<div className="pt-2 tags" >{feed}</div>)
    }
}

class Tag extends React.Component {
    constructor(props) {
        super(props);
        console.log('tag')
        this.state = {
            name: this.props.tag.name,
            id: this.props.tag.id
        }
    };
    render() {
        return(
            <span className="tag">
                {this.state.name}
            </span>
        )
    }
}
view_home();