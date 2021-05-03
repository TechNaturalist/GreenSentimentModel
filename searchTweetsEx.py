from searchtweets import ResultStream, gen_request_parameters, load_credentials

search_args = load_credentials("~/.twitter_keys.yaml",
                                       yaml_key="search_tweets_v2",
                                       env_overwrite=False)

query = gen_request_parameters("Electric Vehicle", results_per_call=100)

rs = ResultStream(request_parameters=query,
                    max_results=500,
                    max_pages=1,
                    **search_args)

tweets = list(rs.stream())

