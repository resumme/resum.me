/*! datatable.js | Bulkit | CSS Ninja */

/* ==========================================================================
Dashboard datatable JS file 
========================================================================== */

$(document).ready(function($){

    "use strict";
    
    if ($('#basic-datatable').length) {
        
        var basicDatatable = new DataTable(document.querySelector('#basic-datatable'), {
            pageSize: 5,
            sort: [true, true, false],
            filters: [true, false, false],
            filterText: 'Type to Filter... ',
            pagingDivSelector: "#paging-basic-datatable",
            firstPage: '<i class="material-icons">arrow_back</i>',
            lastPage: '<i class="material-icons">arrow_forward</i>',
            nextPage: '<i class="material-icons">keyboard_arrow_right</i>',
            prevPage: '<i class="material-icons">keyboard_arrow_left</i>',
            data: [
                {
                    firstname: 'Albert', 
                    lastname: 'Einstein',
                    position: 'Scientist'
                },
                {
                    firstname: 'Linus',  
                    lastname: 'Torvalds',
                    position: 'Scientist'
                },
                {
                    firstname: 'Ada',    
                    lastname: 'Lovelace',
                    position: 'Scientist'
                },
                {
                    firstname: 'Helen',    
                    lastname: 'Miller',
                    position: 'Scientist'
                },
                {
                    firstname: 'John',    
                    lastname: 'Doe',
                    position: 'Scientist'
                },
                {
                    firstname: 'Adam',    
                    lastname: 'Bradley',
                    position: 'Scientist'
                },
                {
                    firstname: 'Steve',    
                    lastname: 'Krucziak',
                    position: 'Scientist'
                }
            ]
        });
        
    }
    
    if ($('#bordered-datatable').length) {
        
        var basicDatatable = new DataTable(document.querySelector('#bordered-datatable'), {
            pageSize: 5,
            sort: [true, true, false],
            filters: [true, false, false],
            filterText: 'Type to Filter... ',
            pagingDivSelector: "#paging-bordered-datatable",
            firstPage: '<i class="material-icons">arrow_back</i>',
            lastPage: '<i class="material-icons">arrow_forward</i>',
            nextPage: '<i class="material-icons">keyboard_arrow_right</i>',
            prevPage: '<i class="material-icons">keyboard_arrow_left</i>',
            data: [
                {
                    firstname: 'Albert', 
                    lastname: 'Einstein',
                    position: 'Scientist'
                },
                {
                    firstname: 'Linus',  
                    lastname: 'Torvalds',
                    position: 'Scientist'
                },
                {
                    firstname: 'Ada',    
                    lastname: 'Lovelace',
                    position: 'Scientist'
                },
                {
                    firstname: 'Helen',    
                    lastname: 'Miller',
                    position: 'Scientist'
                },
                {
                    firstname: 'John',    
                    lastname: 'Doe',
                    position: 'Scientist'
                },
                {
                    firstname: 'Adam',    
                    lastname: 'Bradley',
                    position: 'Scientist'
                },
                {
                    firstname: 'Steve',    
                    lastname: 'Krucziak',
                    position: 'Scientist'
                }
            ]
        });
        
    }
    
    if ($('#striped-datatable').length) {
        
        var basicDatatable = new DataTable(document.querySelector('#striped-datatable'), {
            pageSize: 5,
            sort: [true, true, false],
            filters: [true, false, false],
            filterText: 'Type to Filter... ',
            pagingDivSelector: "#paging-striped-datatable",
            firstPage: '<i class="material-icons">arrow_back</i>',
            lastPage: '<i class="material-icons">arrow_forward</i>',
            nextPage: '<i class="material-icons">keyboard_arrow_right</i>',
            prevPage: '<i class="material-icons">keyboard_arrow_left</i>',
            data: [
                {
                    firstname: 'Albert', 
                    lastname: 'Einstein',
                    position: 'Scientist'
                },
                {
                    firstname: 'Linus',  
                    lastname: 'Torvalds',
                    position: 'Scientist'
                },
                {
                    firstname: 'Ada',    
                    lastname: 'Lovelace',
                    position: 'Scientist'
                },
                {
                    firstname: 'Helen',    
                    lastname: 'Miller',
                    position: 'Scientist'
                },
                {
                    firstname: 'John',    
                    lastname: 'Doe',
                    position: 'Scientist'
                },
                {
                    firstname: 'Adam',    
                    lastname: 'Bradley',
                    position: 'Scientist'
                },
                {
                    firstname: 'Steve',    
                    lastname: 'Krucziak',
                    position: 'Scientist'
                }
            ]
        });
        
    } 
    
    if ($('#narrow-datatable').length) {
        
        var basicDatatable = new DataTable(document.querySelector('#narrow-datatable'), {
            pageSize: 5,
            sort: [true, true, false],
            filters: [true, false, false],
            filterText: 'Type to Filter... ',
            pagingDivSelector: "#paging-narrow-datatable",
            firstPage: '<i class="material-icons">arrow_back</i>',
            lastPage: '<i class="material-icons">arrow_forward</i>',
            nextPage: '<i class="material-icons">keyboard_arrow_right</i>',
            prevPage: '<i class="material-icons">keyboard_arrow_left</i>',
            data: [
                {
                    firstname: 'Albert', 
                    lastname: 'Einstein',
                    position: 'Scientist'
                },
                {
                    firstname: 'Linus',  
                    lastname: 'Torvalds',
                    position: 'Scientist'
                },
                {
                    firstname: 'Ada',    
                    lastname: 'Lovelace',
                    position: 'Scientist'
                },
                {
                    firstname: 'Helen',    
                    lastname: 'Miller',
                    position: 'Scientist'
                },
                {
                    firstname: 'John',    
                    lastname: 'Doe',
                    position: 'Scientist'
                },
                {
                    firstname: 'Adam',    
                    lastname: 'Bradley',
                    position: 'Scientist'
                },
                {
                    firstname: 'Steve',    
                    lastname: 'Krucziak',
                    position: 'Scientist'
                }
            ]
        });
        
    }
    
    if ($('#hoverable-datatable').length) {
        
        var basicDatatable = new DataTable(document.querySelector('#hoverable-datatable'), {
            pageSize: 5,
            sort: [true, true, false],
            filters: [true, false, false],
            filterText: 'Type to Filter... ',
            pagingDivSelector: "#paging-hoverable-datatable",
            firstPage: '<i class="material-icons">arrow_back</i>',
            lastPage: '<i class="material-icons">arrow_forward</i>',
            nextPage: '<i class="material-icons">keyboard_arrow_right</i>',
            prevPage: '<i class="material-icons">keyboard_arrow_left</i>',
            data: [
                {
                    firstname: 'Albert', 
                    lastname: 'Einstein',
                    position: 'Scientist'
                },
                {
                    firstname: 'Linus',  
                    lastname: 'Torvalds',
                    position: 'Scientist'
                },
                {
                    firstname: 'Ada',    
                    lastname: 'Lovelace',
                    position: 'Scientist'
                },
                {
                    firstname: 'Helen',    
                    lastname: 'Miller',
                    position: 'Scientist'
                },
                {
                    firstname: 'John',    
                    lastname: 'Doe',
                    position: 'Scientist'
                },
                {
                    firstname: 'Adam',    
                    lastname: 'Bradley',
                    position: 'Scientist'
                },
                {
                    firstname: 'Steve',    
                    lastname: 'Krucziak',
                    position: 'Scientist'
                }
            ]
        });
        
    } 
    
    if ($('#advanced-datatable').length) {
        
        var datatable = new DataTable(document.querySelector('#advanced-datatable'), {
            pageSize: 5,
            sort: [true, true, false],
            filters: [false, true, true, false, true, false],
            filterText: 'Type to Filter... ',
            pagingDivSelector: "#paging-first-datatable",
            firstPage: '<i class="material-icons">arrow_back</i>',
            lastPage: '<i class="material-icons">arrow_forward</i>',
            nextPage: '<i class="material-icons">keyboard_arrow_right</i>',
            prevPage: '<i class="material-icons">keyboard_arrow_left</i>',
            data: [
                {
                    picture: '<img class="datatable-avatar" src="https://via.placeholder.com/250x250">',
                    firstname: 'Albert', 
                    lastname: 'Einstein',
                    position: 'Scientist',
                    status: '<span class="tag">Available</span>',
                    action: `
                        <div class="dropdown is-right dropdown-trigger">
                            <div class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span class="material-icons">more_vert</span>
                            </div>

                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item">
                                        Manage
                                    </a>
                                    <a class="dropdown-item">
                                        Settings
                                    </a>
                                    <hr class="dropdown-divider">
                                    <a href="#" class="dropdown-item is-flex">
                                        <span class="material-icons">person_add</span>
                                        Invite
                                    </a>
                                </div>
                            </div>
                        </div>

                    `
                },
                {
                    picture: '<img class="datatable-avatar" src="https://via.placeholder.com/250x250">',
                    firstname: 'Linus',  
                    lastname: 'Torvalds',
                    position: 'Scientist',
                    status: '<span class="tag">Busy</span>',
                    action: `
                        <div class="dropdown is-right dropdown-trigger">
                            <div class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span class="material-icons">more_vert</span>
                            </div>

                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item">
                                        Manage
                                    </a>
                                    <a class="dropdown-item">
                                        Settings
                                    </a>
                                    <hr class="dropdown-divider">
                                    <a href="#" class="dropdown-item is-flex">
                                        <span class="material-icons">person_add</span>
                                        Invite
                                    </a>
                                </div>
                            </div>
                        </div>

                    `
                },
                {
                    picture: '<img class="datatable-avatar" src="https://via.placeholder.com/250x250">',
                    firstname: 'Ada',    
                    lastname: 'Lovelace',
                    position: 'Scientist',
                    status: '<span class="tag">Offline</span>',
                    action: `
                        <div class="dropdown is-right dropdown-trigger">
                            <div class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span class="material-icons">more_vert</span>
                            </div>

                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item">
                                        Manage
                                    </a>
                                    <a class="dropdown-item">
                                        Settings
                                    </a>
                                    <hr class="dropdown-divider">
                                    <a href="#" class="dropdown-item is-flex">
                                        <span class="material-icons">person_add</span>
                                        Invite
                                    </a>
                                </div>
                            </div>
                        </div>

                    `
                },
                {
                    picture: '<img class="datatable-avatar" src="https://via.placeholder.com/250x250">',
                    firstname: 'Helen',    
                    lastname: 'Miller',
                    position: 'Scientist',
                    status: '<span class="tag">Offline</span>',
                    action: `
                        <div class="dropdown is-right dropdown-trigger">
                            <div class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span class="material-icons">more_vert</span>
                            </div>

                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item">
                                        Manage
                                    </a>
                                    <a class="dropdown-item">
                                        Settings
                                    </a>
                                    <hr class="dropdown-divider">
                                    <a href="#" class="dropdown-item is-flex">
                                        <span class="material-icons">person_add</span>
                                        Invite
                                    </a>
                                </div>
                            </div>
                        </div>

                    `
                },
                {
                    picture: '<img class="datatable-avatar" src="https://via.placeholder.com/250x250">',
                    firstname: 'John',    
                    lastname: 'Doe',
                    position: 'Scientist',
                    status: '<span class="tag">Offline</span>',
                    action: `
                        <div class="dropdown is-right dropdown-trigger">
                            <div class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span class="material-icons">more_vert</span>
                            </div>

                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item">
                                        Manage
                                    </a>
                                    <a class="dropdown-item">
                                        Settings
                                    </a>
                                    <hr class="dropdown-divider">
                                    <a href="#" class="dropdown-item is-flex">
                                        <span class="material-icons">person_add</span>
                                        Invite
                                    </a>
                                </div>
                            </div>
                        </div>

                    `
                },
                {
                    picture: '<img class="datatable-avatar" src="https://via.placeholder.com/250x250">',
                    firstname: 'Adam',    
                    lastname: 'Bradley',
                    position: 'Scientist',
                    status: '<span class="tag">Offline</span>',
                    action: `
                        <div class="dropdown is-right dropdown-trigger">
                            <div class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span class="material-icons">more_vert</span>
                            </div>

                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item">
                                        Manage
                                    </a>
                                    <a class="dropdown-item">
                                        Settings
                                    </a>
                                    <hr class="dropdown-divider">
                                    <a href="#" class="dropdown-item is-flex">
                                        <span class="material-icons">person_add</span>
                                        Invite
                                    </a>
                                </div>
                            </div>
                        </div>

                    `
                },
                {
                    picture: '<img class="datatable-avatar" src="https://via.placeholder.com/250x250">',
                    firstname: 'Steve',    
                    lastname: 'Krucziak',
                    position: 'Scientist',
                    status: '<span class="tag">Offline</span>',
                    action: `
                        <div class="dropdown is-right dropdown-trigger">
                            <div class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span class="material-icons">more_vert</span>
                            </div>

                            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                                <div class="dropdown-content">
                                    <a href="#" class="dropdown-item">
                                        Manage
                                    </a>
                                    <a class="dropdown-item">
                                        Settings
                                    </a>
                                    <hr class="dropdown-divider">
                                    <a href="#" class="dropdown-item is-flex">
                                        <span class="material-icons">person_add</span>
                                        Invite
                                    </a>
                                </div>
                            </div>
                        </div>

                    `
                }
            ]
        });
        
    }

        
    
    $('.pagination li').click(function(){
        $('.pagination li.is-selected').removeClass('is-selected');
        $(this).addClass('is-selected');
    })

})