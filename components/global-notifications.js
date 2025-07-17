// 全局通知和测试卡片组件
(function() {
    'use strict';

    // 创建推送通知HTML
    function createPushNotificationsHTML() {
        return `
            <!-- 推送通知弹窗 -->
            <div id="chargeNotification" class="push-notification" style="display: none;">
                <div class="push-notification-header">
                    <div class="push-notification-title">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13 10V3L4 14h7v7l9-11h-7z" fill="#00ff88" stroke="#00ff88" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        <span data-i18n="chargeReminder">充电提醒</span><span>——</span><span class="notification-region">NSW</span>
                    </div>
                    <button class="push-notification-close" onclick="closePushNotification('chargeNotification')">
                        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13 1L1 13M1 1l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </button>
                </div>
                <div class="push-notification-content">
                    <p><span class="notification-region">NSW</span><span data-i18n="regionPrice">地区充电价格</span><span class="highlight-number notification-price">$-19</span><span data-i18n="lowPriceCharge">，现在是充电好时机</span></p>
                </div>
            </div>

            <div id="dischargeNotification" class="push-notification" style="display: none;">
                <div class="push-notification-header">
                    <div class="push-notification-title">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3 3h18v18H3V3z" fill="none" stroke="#ffc107" stroke-width="2"/>
                            <path d="M9 9h6v6H9V9z" fill="#ffc107"/>
                        </svg>
                        <span data-i18n="dischargeReminder">放电提醒</span><span>——</span><span class="notification-region">NSW</span>
                    </div>
                    <button class="push-notification-close" onclick="closePushNotification('dischargeNotification')">
                        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13 1L1 13M1 1l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </button>
                </div>
                <div class="push-notification-content">
                    <p><span class="notification-region">NSW</span><span data-i18n="regionPrice">地区放电价格</span><span class="highlight-number notification-price">$436</span><span data-i18n="highPriceDischarge">，现在是放电好时机</span></p>
                </div>
            </div>

            <div id="optimalNotification" class="push-notification" style="display: none;">
                <div class="push-notification-header">
                    <div class="push-notification-title">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="#1e7fff" stroke="#1e7fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        <span data-i18n="optimalReminder">最佳时机提醒</span><span>——</span><span class="notification-region">NSW</span>
                    </div>
                    <button class="push-notification-close" onclick="closePushNotification('optimalNotification')">
                        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13 1L1 13M1 1l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </button>
                </div>
                <div class="push-notification-content">
                    <p><span data-i18n="currentAction">当前</span><span class="notification-action-type">充电</span><span data-i18n="priceIs">价格为</span><span class="highlight-number notification-price">$68</span><span data-i18n="optimalTime">，是今日最佳</span><span class="notification-action-type">充电</span><span data-i18n="opportunity">时机</span></p>
                </div>
            </div>

            <div id="priceAlertNotification" class="push-notification" style="display: none;">
                <div class="push-notification-header">
                    <div class="push-notification-title">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            <line x1="12" y1="9" x2="12" y2="13" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            <line x1="12" y1="17" x2="12.01" y2="17" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        <span class="notification-price-type">高价</span><span class="notification-action-type">充电</span><span data-i18n="priceReminder">提醒</span><span>——</span><span class="notification-region">NSW</span>
                    </div>
                    <button class="push-notification-close" onclick="closePushNotification('priceAlertNotification')">
                        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13 1L1 13M1 1l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </button>
                </div>
                <div class="push-notification-content">
                    <p><span class="notification-region">NSW</span><span data-i18n="regionPrice">地区充电价格</span><span class="highlight-number notification-price">$319</span><span data-i18n="timeRemaining">，还有</span><span class="highlight-value notification-time">27</span><span data-i18n="minutesToPrice">分钟到达</span><span class="notification-price-type">高价</span><span class="notification-action-type">充电</span><span data-i18n="timeOpportunity">时机，请做好准备</span></p>
                </div>
            </div>
        `;
    }

    // 创建测试卡片HTML
    

    // 创建样式
    function createStyles() {
        const style = document.createElement('style');
        style.textContent = `
            /* 推送通知样式 */
            .push-notification {
                position: fixed;
                top: 80px;
                right: 20px;
                width: 400px;
                background: #fff;
                border-radius: 12px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15), 0 2px 10px rgba(0, 0, 0, 0.1);
                padding: 20px;
                z-index: 10001;
                animation: slideInRight 0.3s ease-out;
                border: 1px solid rgba(0, 0, 0, 0.06);
            }

            @keyframes slideInRight {
                from {
                    transform: translateX(120%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }

            .push-notification-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 15px;
                padding-bottom: 15px;
                border-bottom: 1px solid #f0f0f0;
            }

            .push-notification-title {
                display: flex;
                align-items: center;
                gap: 8px;
                font-size: 16px;
                font-weight: 600;
                color: #333;
            }

            .push-notification-close {
                background: none;
                border: none;
                cursor: pointer;
                padding: 4px;
                color: #999;
                transition: color 0.2s;
                border-radius: 4px;
            }

            .push-notification-close:hover {
                color: #666;
                background: #f5f5f5;
            }

            .push-notification-content {
                font-size: 14px;
                line-height: 1.6;
                color: #666;
            }

            .push-notification-content .highlight-number {
                font-size: 24px;
                font-weight: 700;
                margin: 0 8px;
                vertical-align: middle;
            }

            .push-notification-content .highlight-value {
                font-size: 20px;
                font-weight: 600;
                color: #ff6b6b;
                margin: 0 6px;
            }

            #chargeNotification .highlight-number {
                color: #00ff88;
            }

            #dischargeNotification .highlight-number {
                color: #ffc107;
            }

            #optimalNotification .highlight-number {
                color: #1e7fff;
            }

            #priceAlertNotification .highlight-number {
                color: #ff6b6b;
            }

            @media (max-width: 768px) {
                .push-notification {
                    width: calc(100% - 40px);
                    right: 20px;
                    left: 20px;
                }
            }
        `;
        return style;
    }

    // 全局函数：关闭推送通知
    window.closePushNotification = function(notificationId) {
        const notification = document.getElementById(notificationId);
        if (notification) {
            notification.style.display = 'none';
        }
    };

    // 全局函数：显示推送通知
    window.showPushNotification = function(notificationId, duration = 5000) {
        const notification = document.getElementById(notificationId);
        if (notification) {
            notification.style.display = 'block';
            
            if (duration > 0) {
                setTimeout(() => {
                    closePushNotification(notificationId);
                }, duration);
            }
        }
    };

    // 模拟充电提醒
    window.simulateChargeNotification = function() {
        const regions = ['NSW', 'VIC', 'QLD', 'SA'];
        const region = regions[Math.floor(Math.random() * regions.length)];
        const price = Math.floor(Math.random() * 100) - 50;
        
        const notification = document.getElementById('chargeNotification');
        if (notification) {
            const regionElements = notification.querySelectorAll('.notification-region');
            regionElements.forEach(elem => elem.textContent = region);
            
            const priceElement = notification.querySelector('.notification-price');
            if (priceElement) {
                priceElement.textContent = `$${price}`;
            }
            
            showPushNotification('chargeNotification', 8000);
        }
    };

    // 模拟放电提醒
    window.simulateDischargeNotification = function() {
        const regions = ['NSW', 'VIC', 'QLD', 'SA'];
        const region = regions[Math.floor(Math.random() * regions.length)];
        const price = Math.floor(Math.random() * 300) + 200;
        
        const notification = document.getElementById('dischargeNotification');
        if (notification) {
            const regionElements = notification.querySelectorAll('.notification-region');
            regionElements.forEach(elem => elem.textContent = region);
            
            const priceElement = notification.querySelector('.notification-price');
            if (priceElement) {
                priceElement.textContent = `$${price}`;
            }
            
            showPushNotification('dischargeNotification', 8000);
        }
    };

    // 模拟最佳时机提醒
    window.simulateOptimalNotification = function() {
        const regions = ['NSW', 'VIC', 'QLD', 'SA'];
        const region = regions[Math.floor(Math.random() * regions.length)];
        const price = Math.floor(Math.random() * 150) + 50;
        const actionTypes = ['充电', '放电'];
        const actionType = actionTypes[Math.floor(Math.random() * actionTypes.length)];
        
        const notification = document.getElementById('optimalNotification');
        if (notification) {
            const regionElements = notification.querySelectorAll('.notification-region');
            regionElements.forEach(elem => elem.textContent = region);
            
            const priceElement = notification.querySelector('.notification-price');
            if (priceElement) {
                priceElement.textContent = `$${price}`;
            }
            
            const actionElements = notification.querySelectorAll('.notification-action-type');
            actionElements.forEach(elem => elem.textContent = actionType);
            
            showPushNotification('optimalNotification', 8000);
        }
    };

    // 模拟价格提醒
    window.simulatePriceAlertNotification = function() {
        const regions = ['NSW', 'VIC', 'QLD', 'SA'];
        const region = regions[Math.floor(Math.random() * regions.length)];
        const price = Math.floor(Math.random() * 200) + 200;
        const time = Math.floor(Math.random() * 30) + 5;
        const priceTypes = ['高价', '低价'];
        const actionTypes = ['充电', '放电'];
        const priceType = priceTypes[Math.floor(Math.random() * priceTypes.length)];
        const actionType = actionTypes[Math.floor(Math.random() * actionTypes.length)];
        
        const notification = document.getElementById('priceAlertNotification');
        if (notification) {
            const regionElements = notification.querySelectorAll('.notification-region');
            regionElements.forEach(elem => elem.textContent = region);
            
            const priceElement = notification.querySelector('.notification-price');
            if (priceElement) {
                priceElement.textContent = `$${price}`;
            }
            
            const timeElement = notification.querySelector('.notification-time');
            if (timeElement) {
                timeElement.textContent = time;
            }
            
            const priceTypeElements = notification.querySelectorAll('.notification-price-type');
            priceTypeElements.forEach(elem => elem.textContent = priceType);
            
            const actionTypeElements = notification.querySelectorAll('.notification-action-type');
            actionTypeElements.forEach(elem => elem.textContent = actionType);
            
            showPushNotification('priceAlertNotification', 8000);
        }
    };

    // 初始化拖拽功能
    function initTestCardDrag() {
        const container = document.getElementById('testCardContainer');
        const dragHandle = document.getElementById('testCardDragHandle');
        
        if (!container || !dragHandle) return;
        
        let isDragging = false;
        let currentX;
        let currentY;
        let initialX;
        let initialY;
        let xOffset = 0;
        let yOffset = 0;
        
        // 从localStorage恢复位置
        const savedPosition = localStorage.getItem('testCardPosition');
        if (savedPosition) {
            try {
                const pos = JSON.parse(savedPosition);
                const rect = container.getBoundingClientRect();
                const maxX = window.innerWidth - rect.width;
                const maxY = window.innerHeight - rect.height;
                
                const validX = Math.max(0, Math.min(pos.x || 0, maxX));
                const validY = Math.max(0, Math.min(pos.y || 0, maxY));
                
                container.style.bottom = 'auto';
                container.style.left = '0';
                container.style.top = '0';
                container.style.transform = `translate3d(${validX}px, ${validY}px, 0)`;
                xOffset = validX;
                yOffset = validY;
            } catch (e) {
                console.error('Failed to restore test card position:', e);
                localStorage.removeItem('testCardPosition');
            }
        }
        
        function dragStart(e) {
            if (e.type === "touchstart") {
                initialX = e.touches[0].clientX - xOffset;
                initialY = e.touches[0].clientY - yOffset;
            } else {
                initialX = e.clientX - xOffset;
                initialY = e.clientY - yOffset;
            }
            
            if (e.target === dragHandle || dragHandle.contains(e.target)) {
                isDragging = true;
                container.style.cursor = 'grabbing';
            }
        }
        
        function dragEnd(e) {
            initialX = currentX;
            initialY = currentY;
            isDragging = false;
            container.style.cursor = 'auto';
            
            localStorage.setItem('testCardPosition', JSON.stringify({
                x: xOffset,
                y: yOffset
            }));
        }
        
        function drag(e) {
            if (e.preventDefault) {
                e.preventDefault();
            }
            
            if (isDragging) {
                if (e.type === "touchmove") {
                    currentX = e.touches[0].clientX - initialX;
                    currentY = e.touches[0].clientY - initialY;
                } else {
                    currentX = e.clientX - initialX;
                    currentY = e.clientY - initialY;
                }
                
                xOffset = currentX;
                yOffset = currentY;
                
                const rect = container.getBoundingClientRect();
                const maxX = window.innerWidth - rect.width;
                const maxY = window.innerHeight - rect.height;
                
                currentX = Math.max(0, Math.min(currentX, maxX));
                currentY = Math.max(0, Math.min(currentY, maxY));
                
                container.style.bottom = 'auto';
                container.style.transform = `translate3d(${currentX}px, ${currentY}px, 0)`;
            }
        }
        
        dragHandle.addEventListener('mousedown', dragStart);
        document.addEventListener('mouseup', dragEnd);
        document.addEventListener('mousemove', drag);
        
        dragHandle.addEventListener('touchstart', dragStart, { passive: false });
        document.addEventListener('touchend', dragEnd);
        document.addEventListener('touchmove', drag, { passive: false });
    }

    // 重置测试卡片位置
    window.resetTestCardPosition = function() {
        const container = document.getElementById('testCardContainer');
        if (container) {
            container.style.bottom = '20px';
            container.style.left = '20px';
            container.style.top = 'auto';
            container.style.transform = 'none';
            localStorage.removeItem('testCardPosition');
            updateTestCardPosition();
            console.log('Test card position reset to bottom-left corner');
        }
    };

    // 更新测试卡片位置显示
    function updateTestCardPosition() {
        const container = document.getElementById('testCardContainer');
        const positionSpan = document.getElementById('testCardPosition');
        if (container && positionSpan) {
            const rect = container.getBoundingClientRect();
            positionSpan.textContent = `(${Math.round(rect.left)}, ${Math.round(rect.top)})`;
        }
    }

    // 测试工具相关函数
    window.toggleTestTools = function() {
        const panel = document.getElementById('testToolsPanel');
        const toggle = document.getElementById('testToolsToggle');
        if (panel && toggle) {
            if (panel.style.display === 'none' || !panel.style.display) {
                panel.style.display = 'block';
                toggle.style.transform = 'rotate(45deg)';
            } else {
                panel.style.display = 'none';
                toggle.style.transform = 'rotate(0deg)';
            }
        }
    };

    window.closeTestTools = function() {
        const panel = document.getElementById('testToolsPanel');
        const toggle = document.getElementById('testToolsToggle');
        if (panel && toggle) {
            panel.style.display = 'none';
            toggle.style.transform = 'rotate(0deg)';
        }
    };

    window.showTestCard = function() {
        const container = document.getElementById('testCardContainer');
        if (container) {
            container.style.display = 'block';
            updateTestCardPosition();
            console.log('Test card shown');
        }
    };

    window.hideTestCard = function() {
        const container = document.getElementById('testCardContainer');
        if (container) {
            container.style.display = 'none';
            console.log('Test card hidden');
        }
    };

    window.randomTestCard = function() {
        const container = document.getElementById('testCardContainer');
        if (container) {
            const maxX = window.innerWidth - 300;
            const maxY = window.innerHeight - 150;
            const randomX = Math.max(0, Math.floor(Math.random() * maxX));
            const randomY = Math.max(0, Math.floor(Math.random() * maxY));
            
            container.style.bottom = 'auto';
            container.style.left = '0';
            container.style.top = '0';
            container.style.transform = `translate3d(${randomX}px, ${randomY}px, 0)`;
            
            localStorage.setItem('testCardPosition', JSON.stringify({
                x: randomX,
                y: randomY
            }));
            
            updateTestCardPosition();
            console.log(`Test card moved to random position: (${randomX}, ${randomY})`);
        }
    };

    // 自动测试相关
    let autoTestInterval = null;
    const autoTestFunctions = [
        'simulateChargeNotification',
        'simulateDischargeNotification', 
        'simulateOptimalNotification',
        'simulatePriceAlertNotification'
    ];

    window.startAutoTest = function() {
        if (autoTestInterval) {
            clearInterval(autoTestInterval);
        }
        
        console.log('Starting auto test...');
        autoTestInterval = setInterval(() => {
            const randomFunc = autoTestFunctions[Math.floor(Math.random() * autoTestFunctions.length)];
            if (window[randomFunc]) {
                window[randomFunc]();
                console.log(`Auto test triggered: ${randomFunc}`);
            }
        }, 3000); // 每3秒触发一次
        
        console.log('Auto test started - notifications every 3 seconds');
    };

    window.stopAutoTest = function() {
        if (autoTestInterval) {
            clearInterval(autoTestInterval);
            autoTestInterval = null;
            console.log('Auto test stopped');
        }
    };

    // 初始化组件
    function init() {
        // 创建容器
        const container = document.createElement('div');
        container.id = 'globalNotificationsContainer';
        container.innerHTML = createPushNotificationsHTML();
        
        // 添加样式
        document.head.appendChild(createStyles());
        
        // 添加到body
        document.body.appendChild(container);
        
        // 初始化拖拽
        initTestCardDrag();
        
        // 检查卡片是否可见
        setTimeout(() => {
            const testCard = document.getElementById('testCardContainer');
            if (testCard) {
                const rect = testCard.getBoundingClientRect();
                if (rect.right < 0 || rect.bottom < 0 || rect.left > window.innerWidth || rect.top > window.innerHeight) {
                    console.warn('Test card is outside viewport, resetting position...');
                    resetTestCardPosition();
                }
            }
        }, 1000);
        
        // 更新翻译
        if (window.i18n && window.i18n.updateTranslations) {
            setTimeout(() => {
                window.i18n.updateTranslations();
            }, 100);
        }
    }

    // 等待DOM加载完成
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();